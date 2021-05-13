n,x = map(int,input().split())
l = [int(s) for s in input().split()]
ans = 1
height = 0
for i in range(n):
    height += l[i] 
    if height <= x:
        ans += 1
print(ans)