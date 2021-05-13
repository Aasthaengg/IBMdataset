N=int(input())
s=input()
t=input()

ans=""
for i in range(N):
    ans=ans+s[i]

count=0

for i in range(N):
    flag=True
    for j in range(i+1):
        #print(s[N-1-i+j])
        if s[N-1-i+j]==t[j]:
            pass
        else:
            flag=False
    if flag:
        count=i+1
#print(count)
for i in range(count,N):
    ans=ans+t[i]

print(len(ans))