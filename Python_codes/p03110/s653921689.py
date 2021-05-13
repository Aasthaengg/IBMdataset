n = int(input())
x = []
u = []
sum = 0.0
for i in range(n):
    tmp1, tmp2 = input().split()
    x.append(float(tmp1))
    u.append(tmp2)
    if u[i] == "JPY":
        sum += x[i]
    else:
        sum += x[i] * 380000

print(sum)
