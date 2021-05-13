a,b,k=map(int,input().split())
lst=[]
for i in range(a,a+k):
    if i>b:
        break
    lst.append(i)
    print(i)
for i in range(b-k+1,b+1):
    if i<a:
        continue
    if not i in lst:
        print(i)