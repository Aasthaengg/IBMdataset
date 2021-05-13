n = int(input())
a_list = [int(x) for x in input().split()]
count = 0
ans = 0
m = 10 ** 9
for i in range(n):
    if a_list[i] < 0:
        a_list[i] *= -1
        count += 1
    ans += a_list[i]
    if a_list[i] < m:
        m = a_list[i]
if count % 2 == 1:
    ans -= m * 2
print(ans)