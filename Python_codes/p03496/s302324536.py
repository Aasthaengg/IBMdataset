def I(): return int(input())
def MI(): return map(int, input().split())
def LI(): return list(map(int, input().split()))
mod=10**9+7

N=I()
a=LI()

M=0
index=0
for i in range(N):
    if abs(M)<abs(a[i]):
        M=a[i]
        index=i
        
ans=[]
cnt=0
if M>0:
    for i in range(N-1):
        if a[i]>a[i+1]:
            ans.append([index+1,i+2])
            ans.append([index+1,i+2])
            a[i+1]+=M*2
            cnt+=2
            M=a[i+1]
            index=i+1
            
else:
    for i in range(N-1):
        if a[N-i-2]>a[N-i-1]:
            ans.append([index+1,N-i-1])
            ans.append([index+1,N-i-1])
            a[N-i-2]+=M*2
            cnt+=2
            M=a[N-i-2]
            index=N-i-2
            
print(cnt)
for i in range(len(ans)):
    print(' '.join(map(str, ans[i])))
            


