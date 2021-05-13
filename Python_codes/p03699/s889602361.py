N = int(input())
S = []

for i in range(N):
    s = int(input())
    S.append(s)

a = sum(S)
ans = 0

if a % 10 != 0:
    ans = a
else:
    T = [s for s in S if s%10!=0]
    if len(T) == 0:
       ans = 0
    else:
        ans = a-min(T)

print(ans)