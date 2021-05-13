n = int(input())
a = list(map(int, input().split()))
B = [a[i] - i for i in range(n)]
b = sorted(B)[n // 2]
print(sum([abs(B[i] - b) for i in range(n)]))
