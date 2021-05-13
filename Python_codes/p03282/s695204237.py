s=input()
k=int(input())
cnt=0
i=0
while s[i] =="1" and i<=len(s):
    cnt+=1
    i+=1
    if i==len(s):
        break

#print(cnt)
if k<=cnt:
    print(1)
else:
    print(s[i])