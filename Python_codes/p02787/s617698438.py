from sys import stdin
h,n=[int(x) for x in stdin.readline().rstrip().split()]
ab=[]
for i in range(n):
    ab.append([int(x) for x in stdin.readline().rstrip().split()])

ans=[0]*(h+1)
for i in range(1,h+1):
    li = [ans[max(i-j[0],0)]+j[1] for j in ab]
    ans[i]=min(li)

print(ans[h])