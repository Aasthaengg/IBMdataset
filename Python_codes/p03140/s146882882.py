n=int(input())
a=input();b=input();c=input()
x=0
for i in range(n):
  x+=len(list(set([a[i],b[i],c[i]])))-1
print(x)