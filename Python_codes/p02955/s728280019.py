N, K = map(int, input().split())
A = list(map(int, input().split()))

divs = []
maxA = sum(A)
for i in range(1, int(maxA ** 0.5) + 1):
    if maxA % i == 0:
        divs.append(i)
        divs.append(maxA // i)

divs.sort(reverse=True)

for d in divs:
    rest = [a % d for a in A]
    rest.sort(reverse=True)
    restSum = sum(rest) // d
    cnt = 0
    for i in range(restSum):
        cnt += d - rest[i]
    if cnt <= K:
        print(d)
        exit()
