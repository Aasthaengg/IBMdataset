n = int(input())
a = list(map(int, input().split()))

s = min(a)
l = max(a)
print(l - s)