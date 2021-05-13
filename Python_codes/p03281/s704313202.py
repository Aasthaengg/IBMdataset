N = int(input())
if N <= 105:
    if N == 105:
        print(1)
    else:
        print(0)
    exit()
ret = 1
for i in range(107, N+1, 2):
    div = 0
    for j in range(1, i+1, 2):
        if i%j==0:
            div += 1
    if div == 8:
        ret += 1
print(ret)
