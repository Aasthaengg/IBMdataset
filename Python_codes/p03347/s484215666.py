N = int(input())
data = [int(input()) for i in range(N)]
c = 0
if data[0] > 0:
    print(-1)
    exit()
for i in range(1,N)[::-1]:
    if data[i] - data[i-1] > 1:
        print(-1)
        exit()
    if data[i] - data[i-1] == 1:
        c += 1
    if data[i] - data[i-1] < 1:
        c += data[i]
print(c)
