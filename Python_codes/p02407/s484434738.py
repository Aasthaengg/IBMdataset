n = int(input())
lis = list(map(int, input().split()))

for i in range(n - 1):
    print(lis[n - i - 1], end=" ")
print(lis[0])