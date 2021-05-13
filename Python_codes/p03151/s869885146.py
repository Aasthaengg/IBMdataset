n = int(input())
A = list(map(int, input().split()))
sumA = sum(A)
B = list(map(int, input().split()))
sumB = sum(B)

if sumA < sumB:
    print(-1)
    exit(0)

# 条件確認する
flag = True
ok = []
not_ok = []
not_ok_sum = 0
for i in range(n):
    if A[i] < B[i]:
        not_ok.append(i)
        not_ok_sum += A[i]
        flag = False
    else:
        ok.append(A[i] - B[i])

if flag:
    print(0)
    exit(0)

ok.sort()
ok.reverse()

# print(n)
# print(A)
# print(B)
# print(not_ok)
# print(not_ok_sum)
# print(sumA - not_ok_sum)
# print(ok)

# 残っている余力の大きい方から順番に使って，足りていない分を埋めていく
count = 0
current = 0
now_prev = 0
rem = 0
while True:
    now = now_prev + ok[current]
    count += 1
    # print(current, now)
    while rem < len(not_ok):
        j = not_ok[rem]
        # print("  ", j, B[j] - A[j])
        if B[j] - A[j] < now:
            rem += 1
            now -= (B[j] - A[j])
            # print(now)
            count += 1
        else:
            break
    if rem == len(not_ok):
        break
    else:
        now_prev = now
        current += 1
print(count)