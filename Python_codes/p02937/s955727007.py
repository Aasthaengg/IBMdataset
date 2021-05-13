from bisect import bisect_left, bisect_right
import sys

def solve():
    numChar = 26
    ordA = ord('a')

    Ss = input().rstrip()
    Ts = input().rstrip()

    lenS = len(Ss)
    Ss = [ord(S)-ordA for S in Ss]
    Ts = [ord(T)-ordA for T in Ts]

    setS, setT = set(Ss), set(Ts)
    for T in setT:
        if T not in setS:
            print(-1)
            sys.exit()

    posChs = [[] for _ in range(numChar)]
    for i, S in enumerate(Ss+Ss):
        posChs[S].append(i)

    ans = 0
    i = -1
    for T in Ts:
        iPos = bisect_right(posChs[T], i)
        i2 = posChs[T][iPos]
        ans += i2 - i
        i = i2 % lenS

    print(ans)


solve()
