n = int(input())
a = list(map(int, input().split()))
ave = sum(a) / n
b = [abs(a[i] - ave) for i in range(n)]
print(b.index(min(b)))