N=int(input())

ans=N/1.08

ans=int(ans)
flag=True

while flag:
    if int(ans*1.08)<N:
        ans+=1
    elif int(ans*1.08)==N:
        break
    else:
        print(':(')
        flag=False
    
if flag:
    print(ans)
