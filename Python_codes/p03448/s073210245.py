a=int(input())
b=int(input())
c=int(input())
d=int(input())
ans=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*500+j*100+k*50==d:
                ans+=1
print(ans)