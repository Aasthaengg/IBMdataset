n=int(input())
a=[list(input())for i in range(3)]
cnt=0
for i in range(n):
    tmp=[]
    tmp.append(a[0][i])
    tmp.append(a[1][i])
    tmp.append(a[2][i])
    cnt+=len(list(set(tmp)))-1
print(cnt)
