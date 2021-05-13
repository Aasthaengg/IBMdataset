n = int(input())
T = list(map(int, input().split()))
A = list(map(int, input().split()))
MOD = 10**9+7
only = [False]*n
h = [0]*n
mx = 0
for i, t in enumerate(T):
    if t > mx:
        only[i] = True
        h[i] = t
        mx = t
    else:
        h[i] = t

mx = 0
for i, a in enumerate(A[::-1]):
    k = n-i-1
    if only[k]:
        if a > mx:
            if h[k] != a:
                print(0)
                exit()
            else:
                mx = a
                continue
        else:
            if h[k] <= a: continue
            else:
                print(0)
                exit()
    else:
        if a > mx:
            if a <= h[k]:
                only[k] = True
                h[k] = a
                mx = a
            else:
                print(0)
                exit()
        else:
            if a <= h[k]:
                h[k] = a

ans = 1
for i in range(n):
    if only[i]: continue
    ans *= h[i]
    ans %= MOD
print(ans)