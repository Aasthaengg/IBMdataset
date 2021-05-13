n=int(input())
if n==1:
    print('Yes')
    print(2)
    print(1,1)
    print(1,1)
    exit()
if n==2:
    print('No')
    exit() 
a=[[1]]
i=1
for j in range(1,n):
    a.append(list(range(i,i+j)))
    if n==i+j-1:
        break
    elif i+j>n:
        print('No')
        exit()
    i+=j
print('Yes')
m=len(a)
for i in range(m-1):
    for j in range(i+1+(i<1),m):
        a[i].append(a[j][i])
print(m)
for b in a:
    print(len(b),*b)