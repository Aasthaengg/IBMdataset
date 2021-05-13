n = int(input())
S = list(map(int, input().split()))
q = int(input())
T = list(map(int, input().split()))


def linear_search(series, key):
    for x in series:
        if key == x:
            return 1
    return 0

cnt = 0
for t in T:
    cnt += linear_search(S, t)
print(cnt)
