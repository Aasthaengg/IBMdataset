n = int(input())

unit = 10
cnt = 0
flg = 1

for i in range(1,n+1):
    if i//unit < 1:
        if flg==1:
            cnt+=1
    else:
        unit*=10
        flg^=1
        if flg==1:
            cnt+=1

print(cnt)