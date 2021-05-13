X, N = map(int, input().split())
if N == 0:
    print(X)
    exit()

p = list(map(int, input().split()))
count = 0
res = 0
while True:
    before = X - count
    after = X + count
    if before not in p:
        res = before
        break
    elif after not in p:
        res = after
        break
    count += 1
print(res)
