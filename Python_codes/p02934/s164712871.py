n = int(input())
A = list(map(int, input().split()))
pans = 0
for i in A:
    pans += 1 / i
print(1 / pans)