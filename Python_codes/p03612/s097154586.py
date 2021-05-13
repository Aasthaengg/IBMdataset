n = int(input()) 
p = list(map(int,input().split()))

ans = 0
skip = False
for i in range(n):
    if skip:
        skip = False
        continue
    if i+1 == p[i]:
        ans += 1
        skip = True

print(ans)
