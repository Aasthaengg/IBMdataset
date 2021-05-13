n = int(input())
a = list(map(int, input().split()))

ans = 0
for a_i in a:
    a_i_tmp = a_i
    while a_i_tmp % 2 == 0:
        ans += 1
        a_i_tmp /= 2
print(ans)
