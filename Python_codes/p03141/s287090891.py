n = int(input())
abc =[]
for i in range(n):
    a,b = [int(x) for x in input().split()]
    abc.append([a,b,a+b])
abc = sorted(abc,key=lambda x: x[2],reverse=True)
t=0
a=0
for i in range(n):
    if i%2==0:
        t+=abc[i][0]
    else:
        a+=abc[i][1]
print(t-a)