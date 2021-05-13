n=int(input())
c=list(map(int, input().split())) 

ans = 1
b = c[0]

for i in range(1,n):
    if b >=c[i]:
        b = c[i]
        ans +=1
    else:
        pass

print(ans)