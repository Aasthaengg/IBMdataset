S = input()
K = int(input())

def f(S):
    cnt = 0
    t = 0
    for i in range(1, len(S)):
        if S[i-1] == S[i]:
            t += 1
        else:
            t = 0
        if t % 2 == 1:
            cnt += 1
    return cnt

if len(set(S)) == 1:
    l = len(S) * K
    print(l // 2)
elif K < 10:
    print(f(S * K))
else:
    v2 = f(S * 2)
    v3 = f(S * 3)
    print(v3 + (v3-v2) * (K - 3))
