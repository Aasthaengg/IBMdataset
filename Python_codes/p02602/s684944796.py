n, k = map(int, input().split())
a = list(map(int, input().split()))
print(*['Yes' if a[i] < a[k + i] else 'No' for i in range(n - k)], sep='\n')