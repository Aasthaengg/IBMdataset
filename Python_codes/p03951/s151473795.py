N=int(input())
s=input()
t=input()
res=N*2
for i in range(1,N+1):
    if(t[:i]==s[N-i:]):
        res=N*2-i
print(res)