s=list(input())
t=list("CODEFESTIVAL2016")
cnt=0
for i in range(16):
    if(s[i]!=t[i]):
        cnt+=1
print(cnt)