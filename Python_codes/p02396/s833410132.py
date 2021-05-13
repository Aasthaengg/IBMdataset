a =[]
x = 1
while x > 0:
    x = int(input())
    a.append(x)
for i in range(0,len(a)-1):
    print('Case ',i+1,': ',a[i],sep='')