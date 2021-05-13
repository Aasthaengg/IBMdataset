n = int(input())
p = list(map(int, input().split()))
 
l = p[0]
ans = 0
for i in p:
    if i <= l:
        ans += 1
        l = i
print(ans)