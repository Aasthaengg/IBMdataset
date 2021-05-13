l = list(map(int, input().split()))
ans = 0
while( l[0]%2==0 and l[1]%2==0 and l[2]%2==0):
    if l[0]==l[1]and l[1]==l[2]:
        ans = -1
        break
    else:
        a = l[0]
        b = l[1]
        c = l[2]
        l[0]=(b+c)/2
        l[1]=(a+c)/2
        l[2]=(a+b)/2
        ans+=1
print(ans)