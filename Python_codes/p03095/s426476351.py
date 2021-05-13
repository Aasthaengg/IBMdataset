mod = 10**9+7

n = int(input())
S = input()

alp = [chr(i) for i in range(97, 97+26)]

cnt = []
for a in alp:
    cnt.append(S.count(a))

ans = 1
for c in cnt:
    if c:
        ans *= (c+1)

print((ans-1)%mod)