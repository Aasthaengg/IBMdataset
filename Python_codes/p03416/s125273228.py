# input
A, B = map(int, input().split())

# check
cnt = 0
for n in range(A, B + 1):
    if str(n) == str(n)[::-1]:
        cnt += 1

print(cnt)
