N = int(input())
K = int(input())

cnt = 0
val = 1
while cnt < N:
    if val <= K:
        val *= 2
    else:
        val += K
    cnt += 1

print(val)
