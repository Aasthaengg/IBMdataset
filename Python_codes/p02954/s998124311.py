s = input()
a = []
lr=0
ch = 1
for i in range(1,len(s)):
    if (lr%2==0 and s[i]=='R') or (lr%2==1 and s[i]=='L'):
        ch+=1
    else:
        lr+=1
        a.append(ch)
        ch=1
if sum(a)!=len(s):
    a.append(ch)
ans=[]
for i in range(len(a)//2):
    x=a[i*2]
    y=a[i*2+1]
    ans+=['0']*(x-1)
    ans+=[str(x//2+x%2+y//2),str(x//2+y//2+y%2)]
    ans+=['0']*(y-1)
print(' '.join(ans))
