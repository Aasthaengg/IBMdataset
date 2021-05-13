n=int(input())
a=input()
b=input()
p=True
for i in range(n):
    if a[:i]+b[:n-i]==a:
        print(i+n)
        p=False
        break
if p:print(2*n)