B = 380000
N = int(input())
res = 0
for _ in range(N):
    x, v = input().split()
    x = float(x)
    if v=="JPY":
       res += x
    else:
        res += x*B
print(res)