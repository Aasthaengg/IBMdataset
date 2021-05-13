n,h,w = map(int,input().split())
ab_inputs = [list(map(int,input().split())) for i in range(n)]

ans=0
for i in range(n):
    a,b = map(int,ab_inputs[i])
    if a>=h and b>=w:
        ans+=1
print(ans)