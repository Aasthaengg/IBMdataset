n = int(input())
a_list = [int(x) for x in input().split()]
temp_list = [0] * n
temp_list[0] = a_list[0]
for i in range(1, n):
    temp_list[i] = a_list[i] + temp_list[i - 1]
ans = 10 ** 15
for i in range(n - 1):
    temp = abs(temp_list[-1] - (temp_list[i] << 1))
    if temp < ans:
        ans = temp
print(ans)