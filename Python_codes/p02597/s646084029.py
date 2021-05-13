N = int(input())
c = list(input())
a=0; b=0; ans = 0

for i in range(N):
    if c[i] == "R":
        a += 1
ans = max(a,b)

for i in range(N):
    if c[i] == "R":
        a -= 1
    else:
        b += 1
    now = max(a,b)
    ans = min(ans,now)
print(ans)