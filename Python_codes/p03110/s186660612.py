n = int(input())
ansj = 0
ansb = 0
for i in range(n):
    x,u = input().split()
    if u == "JPY":
        ansj += int(x)
    else:
        ansb += float(x)
ansb*=380000
ansj = float(ansj)
print(ansj+ansb)