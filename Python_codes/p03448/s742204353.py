a = int(input())
b = int(input())
c = int(input())
x = int(input())/50
ans=0
for i in range(a+1):
    for j in range(b+1):
        for k in range(c+1):
            if i*10+j*2+k==x:
                ans+=1
print(ans)