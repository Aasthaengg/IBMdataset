N=int(input())
ans='second'
for i in range(0,N):
    a=int(input())
    if a%2==1:
        ans='first'

print(ans)
