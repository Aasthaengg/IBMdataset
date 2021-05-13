from collections import Counter

N,P = map(int,input().split())
S = input()

def two_or_five():
    global S,N,P
    ans = 0
    for k,v in enumerate(S):
        v = int(v)
        if v % P:
            continue
        ans += k + 1
    return ans

def other():
    global S,N,P
    S = reversed(S)
    T = [0] * N
    a = 1
    for k,v in enumerate(S):
        T[k] = T[k-1] + a * int(v)
        T[k] %= P
        a *= 10
        a %= P
    T.append(0)
    ans = 0
    for k,v in Counter(T).items():
        ans += v * (v-1) // 2
    return ans

if P in {2,5}:
    print(two_or_five())
else:
    print(other())