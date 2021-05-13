k, s = map(int, input().split())
 
ans = 0
for x in range(k+1):
    if x > s:
        break
    if x+k+k < s:
        continue
    for y in range(k+1):
        ans += max(0, 0<=s-x-y<=k)
print(ans)