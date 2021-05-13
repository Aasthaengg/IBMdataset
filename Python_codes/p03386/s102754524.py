a,b,k=map(int,input().split())
num=set()
for i in range(a,min(a+k,b+1)):
    num.add(i)
for j in range(max(a,b-k+1),b+1):
    num.add(j)
for i in sorted(list(num)):
    print(i)