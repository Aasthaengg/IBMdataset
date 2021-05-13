S = list(str(input()))
K = int(input())

ones = 0
v = 0
for s in S:
    if s == '1':
        ones += 1
    else:
        v = s
        break

if ones >= K:
    print(1)
else:
    print(v)