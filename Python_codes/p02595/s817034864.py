N, D = map(int, input().split())
i = 0
count = 0
while (i < N):
    p, q = map(int, input().split())
    d = (p*p + q*q) ** 0.5
    if (d <= D):
        count+= 1
    i+= 1
print(count)