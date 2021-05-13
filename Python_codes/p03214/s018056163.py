N = int(input())
a = list(map(int, input().split()))

ave = sum(a) / N
check = []

for i in range(N):
    check.append([abs(ave - a[i]), i])

check.sort()
print(check[0][1])