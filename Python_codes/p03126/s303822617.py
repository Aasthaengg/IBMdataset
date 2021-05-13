n, m = map(int, input().split())

cnt = [0] * m
for i in range(n):
    k, *a = map(int, input().split())
    for a_ in a:
        cnt[a_ - 1] += 1
        
print(sum(c == n for c in cnt))