N = int(input())

sum = 0.0
for _ in range(N):
    x,u = input().split()
    x = float(x)
    if u=="JPY":
        sum = x + sum
        continue
    x = 380000*x
    sum = sum + x
print(sum)