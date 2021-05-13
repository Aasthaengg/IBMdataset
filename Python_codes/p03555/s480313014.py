s1=input()
s2=input()

cnt=0
for i in range(len(s1)):
    if s1[i]==s2[-i-1]:
        cnt+=1

if cnt == 3:
    print("YES")
else:
    print("NO")