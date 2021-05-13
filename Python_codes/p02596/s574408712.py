# ABC174 C

K=int(input())

res=1
r=7%K
flg=(K%2==0 or K%5==0)
if flg:
    res=-1
while not flg:
    if not r:
        break
    r=(10*r+7)%K
    res+=1
print(res)