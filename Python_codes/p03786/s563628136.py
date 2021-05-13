n=int(input())
a=list(map(int,input().split()))
a.sort()
temp=[a[0]]
for i in range(n-1): temp.append(temp[i]+a[i+1])
a.sort(reverse=True)
temp.reverse()
flag=1
for i in range(n-1):
    if a[i]>2*a[i+1] and a[i]>2*temp[i+1]:
        flag=0
        print(i+1)
        break
if flag: print(n)