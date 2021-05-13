s=list(input())
t=list(input())
nmb=[0, 1, 2]
cnt=0
for i in nmb:
    if s[i]==t[i]:
        cnt+=1
print(cnt)
