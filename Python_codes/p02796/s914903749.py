N = int(input())
arms = []
ans = 1
for i in range(N):
    X,L = (int(x) for x in input().split())
    arms.append((X-L,X+L))
arms.sort(key=lambda x:x[1])
limit = arms[0][1]
for x in arms[1:]:
    if x[0] < limit:
        continue
    else:
        limit = x[1]
        ans += 1
print(ans)