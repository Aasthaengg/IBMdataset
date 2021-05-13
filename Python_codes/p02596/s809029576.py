k = int(input())
n = 7
if k == 1 or k == 7:
    print(1)
    exit()
for i in range(1,k+1):
    n = n*10 + 7
    if n % k == 0:
        print(i+1)
        exit()
    n %= k

print(-1)
