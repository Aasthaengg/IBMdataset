n = int(input())
a = [int(i) for i in input().split()]
print(sum(a[i] % 2 == 1 for i in range(0, n, 2)))