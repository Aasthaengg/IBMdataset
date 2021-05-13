n=int(input())
a=[int(input()) for i in range(n)]
cnt=0
button=0
flag=False
#ボタン1が最初光っている(インデックスは0)
for i in range(n):
    #ボタンを押す
    cnt+=1
    button=a[button]-1
    if button==1:
        flag=True
        break
if flag:
    print(cnt)
else:
    print(-1)