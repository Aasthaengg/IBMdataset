N = int(input())
A, B = map(int, input().split())
P = list(map(int, input().split()))
cnt = [0, 0, 0]
for p in P:
    if p <= A:
        cnt[0] += 1
    elif p <= B:
        cnt[1] += 1
    else:
        cnt[2] += 1
print(min(cnt))