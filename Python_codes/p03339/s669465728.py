#https://atcoder.jp/contests/abc098/tasks/arc098_a
n=int(input())
s=input()

"""ans=100000000000
for i in range(n):
    count=0
    for j in range(n):
        if i==j:
            continue

        if (i<j)&(s[j]=="E"):
            count+=1
        elif (j<i)&(s[j]=="W"):
            count+=1

    ans=min(ans,count)

print(ans)"""#O(N^2)

count_W=[]
for i in range(n):
    count_W.append(0)

if s[0]=="W":
    count_W[0]=1
else:
    count_W[0]=0

for i in range(1,n):
    if s[i]=="W":
        count_W[i]=count_W[i-1]+1
    else:
        count_W[i]=count_W[i-1]

for i in range(n):
    if i==0:
        ans=(n-1)-(count_W[n-1]-count_W[0])
    else:
        ans=min(ans,count_W[i-1]+(n-1-i)-(count_W[n-1]-count_W[i]))

print(ans)