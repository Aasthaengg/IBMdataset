k=int(input())
a,b=map(int,input().split())
ans='NG'
while b>=a:
    if a%k==0:
        ans='OK'
        a+=1
    else:
        a+=1
        continue
print(ans)