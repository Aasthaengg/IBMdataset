n=int(input())
cnt=0
flg=False
for _ in range(n):
    d1,d2=map(int,input().split())
    if d1==d2:
        cnt+=1
    else:
        cnt=0
    if cnt>=3:
        flg=True
        break
print("Yes") if flg else print("No")