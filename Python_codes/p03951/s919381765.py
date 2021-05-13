n=int(input())
f=input()
b=input()
for x in range(n):
    if f[x:]==b[:n-x]:print(n+x);break
else:print(n*2)