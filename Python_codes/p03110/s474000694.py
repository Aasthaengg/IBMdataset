n=int(input())
c=0
for i in range(n):
    a,b=input().split()
    if b=="JPY":
        c+=float(a)
    else:
        c+=float(a)*380000
print(c)

