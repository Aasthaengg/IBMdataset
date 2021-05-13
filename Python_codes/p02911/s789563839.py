n, k, q = list(map(int, input().split()))

correct = {}
for parti in range(1, n+1):
    correct[parti] = 0

for i in range(q):
    a = int(input())
    correct[a] += 1

for parti in range(1, n+1):
    if k - q + correct[parti] > 0:
        print("Yes")
    else:
        print("No")
