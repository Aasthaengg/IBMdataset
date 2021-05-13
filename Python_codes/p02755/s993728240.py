a,b = map(int,input().split())

bb = b * 10

ans = -1
for i in range(bb, bb+10):
    if i*8//100==a:
        ans=i
        break

print(ans)
