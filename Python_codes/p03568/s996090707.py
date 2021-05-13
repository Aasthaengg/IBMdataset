n = int(input())
a = list(map(int, input().split()))

ans = 3 ** n - 2 ** len([i for i in a if i%2 == 0])

print(ans)