import sys

def solve():
    input = sys.stdin.readline
    N, P = map(int, input().split())
    S = list(input().strip("\n"))

    if P == 2 or P == 5:
        count = 0
        for i in range(N):
            s = int(S[N - 1 - i])
            if s % P == 0: count += N - i
        print(count)
    else:
        modDict = dict()
        modDict[0] = 1
        sSum = 0
        for i in range(N):
            s = int(S[N - 1 - i])
            sSum += s * pow(10, i, P)
            sSum %= P
            if sSum in modDict: modDict[sSum] += 1
            else: modDict[sSum] = 1
        count = 0
        for key in modDict:
            count += modDict[key] * (modDict[key] - 1) // 2
        print(count)
            

    return 0

if __name__ == "__main__":
    solve()