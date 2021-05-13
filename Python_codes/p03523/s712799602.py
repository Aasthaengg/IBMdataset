S=input()
N=len(S)

if N<=4 or N>=10:
    print("NO")
    exit()

li=["AKIH","KIH"]
lis=[]
ans=[]
for i in range(len(li)):
    lis.append(li[i]+"AB")
    lis.append(li[i]+"B")

for i in range(len(lis)):
    ans.append(lis[i]+"R")
    ans.append(lis[i]+"AR")
    ans.append(lis[i]+"ARA")
    ans.append(lis[i] + "RA")

if S in ans:
    print("YES")
else:
    print("NO")

