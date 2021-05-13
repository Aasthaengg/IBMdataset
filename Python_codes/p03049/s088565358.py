n = int(input())
s= [input() for i in range(n)]
ans1=0
firstB=0
lastA=0
m=n
for i in s:
    ans1+=i.count("AB")
    if i[0]=="B":
        firstB+=1
    if i[-1]=="A":
        lastA+=1
    if i[0]!="B" and i[-1]!="A":
        m-=1
if min(firstB,lastA)==m:
    if m==0:
        print(ans1)
    else:
        print(ans1+m-1)
else:
    print(ans1+min(firstB,lastA))