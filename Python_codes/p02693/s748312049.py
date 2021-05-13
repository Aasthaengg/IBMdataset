k=int(input())
a,b=map(int,input().split())

ans="NG"
for i in range(1,b+1):
    z=i*k
    if a<=z<=b:
        ans="OK"
        break

print(ans)
