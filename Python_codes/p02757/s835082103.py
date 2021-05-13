from collections import Counter

N, P = map(int, input().split())
S = input()

ans = 0

if P==2:
    for i in range(1, N+1):
        v = int(S[-i])
        if v%2==0:
            ans += N-(i-1)
elif P==5:
    for i in range(1, N+1):
        v = int(S[-i])
        if v%5==0:
            ans += N-(i-1)
else:
    ac = [0]*(N+1)
    for i in range(1, N+1):
        ac[i] = (ac[i-1]+int(S[-i])*pow(10, i-1, P))%P
    c = Counter(ac)
    for i in c.values():
        ans += i*(i-1)//2

print(ans)