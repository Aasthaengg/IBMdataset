N, K = map(int, input().split())
d = (N-1)*(N-2)//2 - K
if d < 0:
    print(-1)
    exit()

print(N-1 + d)
for i in range(2, N+1):
    print(1, i)
j = 2
while True:
    for k in range(j+1, N+1):
        if d > 0:
            print(j, k)
            d -= 1
        else:
            break
    if d == 0:
        break
    else:
        j += 1