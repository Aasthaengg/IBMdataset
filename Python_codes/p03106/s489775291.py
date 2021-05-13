a, b, k = map(int, input().split())
ans_list = []

if a > b:
    a, b = b, a

for i in range(a, 0, -1):
    if a % i == 0 and b % i == 0:
        ans_list.append(i)
        if len(ans_list) == k:
            print(i)
            break
