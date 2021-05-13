N = int(input())
As = list(map(int, input().split()))
preans = [0 for _ in range(N)]
for a in As:
    preans[a-1] += 1
for n in preans:
    print(n)