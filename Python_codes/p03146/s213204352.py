s=int(input())
n=set()
a=s
for i in range(10**7):
    if a in n:
        break
    if a%2:
        n.add(a)
        a=3*a+1
    else:
        n.add(a)
        a//=2
print(i+1)