n = int(input())
a, b = map(int, input().split())
p = list(map(int, input().split()))

cnt = [0]*3

for pp in p:
    if pp <= a: cnt[0] += 1
    elif pp <= b: cnt[1] += 1
    else: cnt[2] += 1
print(min(cnt))
