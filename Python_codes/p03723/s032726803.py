a, b, c = map(int, input().split())

if any(i % 2 != 0 for i in [a, b, c]):
    print(0)
    exit()

if a == b and b == c:
    print(-1)
    exit()

cnt = 0
a_list = [0]*(1001001)
b_list = [0]*(1001001)
c_list = [0]*(1001001)
a_list[0] = a
b_list[0] = b
c_list[0] = c

for i in range(1, 1001001):
    a_list[i] = (b_list[i-1] + c_list[i-1]) // 2
    b_list[i] = (c_list[i-1] + a_list[i-1]) // 2
    c_list[i] = (a_list[i-1] + b_list[i-1]) // 2
    cnt += 1
    if a_list[i] % 2 != 0 or b_list[i] % 2 != 0 or c_list[i] % 2 != 0:
        break

print(cnt)
