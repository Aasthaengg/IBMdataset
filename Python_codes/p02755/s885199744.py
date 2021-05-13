A,B=map(int,input().split())
flag=0
for i in range(1,1001):
    if int(i*0.08)==A and int(i*0.1)==B:
        flag=1
        print(i)
        break
if flag==0:
    print(-1)