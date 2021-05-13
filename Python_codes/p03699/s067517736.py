N = int(input())
s = sorted([int(input()) for _ in range(N)])

all_10 = True
for i in range(N):
    if s[i] % 10 != 0:
        all_10 = False

if all_10:
    print(0)
    exit()

sum_s = sum(s)

if sum_s % 10 != 0:
    print(sum_s)
else:
    for i in range(N):
        if s[i] % 10 != 0:
            print(sum_s - s[i])
            break
