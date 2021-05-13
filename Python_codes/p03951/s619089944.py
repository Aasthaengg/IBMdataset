n=int(input())
s=input()
t=input()
flg=True
tmp=0
if s==t:
    print(n)
    exit()
for i in range(1,n):
    ss=s[i:]
    tt=t[:-i]
    if ss==tt:
        print(2*n-len(ss))
        exit()
print(n*2)