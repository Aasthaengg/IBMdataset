n = int(input())
a = list(map(int, input().split()))
c = [0]*(10**6 + 1)

for i in a:
    c[i] += 1

cnt = 0

for i in range(2, 10**6 + 1):
    s = sum(c[i::i])
    if s == n:
        print("not coprime")
        exit()
    elif s > 1:
        cnt += 1

if cnt > 0:
    print("setwise coprime")
else:
    print("pairwise coprime")