N=int(input())
s=str(input())
t=str(input())
c=0
tmp=0
S=list(s)
T=list(t)
for i in range(N):
    if s[N-i-1:N]==t[0:i+1]:
        c=i+1
    #print(s[N-i-1:N],t[0:i+1])
#print(c)
print(2*N-c)
        
