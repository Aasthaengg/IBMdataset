n=int(input())
b=list(map(int,input().split()))
a=[]
flg=1
for i in range(n):
    if flg==0:
        break
    else:
        flg=0
    for j in range(len(b)):
        #print(i,j)
        if b[len(b)-1-j]==len(b)-j:
            a.append(b[len(b)-1-j])
            b=b[:len(b)-1-j]+b[len(b)-j:]
            #print(b,a)
            flg=1
            break
if flg==0:
    print(-1)
else:
    for i in range(n):
        print(a[n-1-i])