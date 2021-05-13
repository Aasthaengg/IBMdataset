n, k = map(int, input().split())
final = 0
x = sorted(list(map(int, input().split())))
for i in range(0, k):
    final += x[i]

print(final)