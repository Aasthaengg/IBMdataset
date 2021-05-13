s=input()
n=len(s)
cnt=0
satan=0
for i in range(n):
    if s[i]=="W":
        cnt+=i-satan
        satan+=1
print(cnt)
