k, t = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

b = 0
for i in a[::-1]:
    b = abs(b-i)
print(max(b-1, 0))
