# n=int(input())
# lst=[int(input()) for _ in range(n)]
# ans1=sum(lst)
# max1=max(lst)
# print(ans1)
# print(0 if max1<=ans1-max1 else max1-(ans1-max1))
s=input()
n=len(s)
l=n-1
lst_1=[]
for i in range(1<<l):
    lst=[]
    for j in range(l):
        if ((i>>j)&1):
            lst.append("+")
        else:lst.append("_")
    lst_1.append(lst)

ans=0
for i in range(1<<l):
    temp=s[0]
    for j in range(l):

        if lst_1[i][j]=="+":
            temp+="+"
        temp += s[j+1]
    ans+=sum(map(int,temp.split("+")))
print(ans)