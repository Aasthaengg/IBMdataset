n, k = map(int, input().split())
s = set(range(1, n+1))
for _ in range(k):
    d = int(input())
    for i in input().split():
        s.discard(int(i))
print(len(s))