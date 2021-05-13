n=int(input())
s=0
for i in range(n):
    x,u=input().split()
    if u=="JPY":
        s=s+int(x)
    else:
        s=s+float(x)*380000.0
print(s)