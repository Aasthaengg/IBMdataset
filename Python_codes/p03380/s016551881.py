n = int(input())
a = list(map(int, input().split()))
maxa = max(a)
mini = [[] for _ in range(n)]
for i, v in enumerate(a):
    r = maxa - v
    mini[i] = [v, abs(v - r)]
mini.sort(key=lambda x: x[1])
if n == 2:
    print(maxa, min(a))
else:
    print(maxa, mini[0][0])
