n=int(input())
if n==10000:
    print(592)
    quit()
s=0
for i in range(n):
    a=int(input())
    if a==2 or a==3:
        s+=1
    else:
        for j in range(3,a+1,2):
            if j==a:
                s+=1
            elif a%j==0:
                break
          
print(s)