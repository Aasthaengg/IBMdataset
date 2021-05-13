n = int(input())
li = list(map(int,input().split()))

li.reverse()

ope=0
flg=0

for i in range(1,n):
    chk = li[i]-li[i-1]
    if chk>1:
        print('No')
        flg = 1
        break
    elif chk==1:
        li[i]-=1
    else:
        continue

if flg==0:
    print('Yes')