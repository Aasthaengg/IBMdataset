N = int(input())
a = list(map(int, input().split()))
a.sort(reverse = True)
b = a[0] - a[N-1]
print(b)