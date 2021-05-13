n=int(input())
lists=[0 for i in range(n)]
for i in range(n):
    a=int(input())
    lists[i]=a
flag=True
for i in range(n):
    if lists[i]%2!=0:
        flag=False
        break
if flag:
    print("second")
else:
    print("first")