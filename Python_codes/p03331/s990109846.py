
def sum_N(a:int):
    sum = 0
    while a > 0:
        sum += a % 10
        a = a // 10
    return sum

N = int(input())
ans = []
for i in range(1, N):
    j = N - i
    ans.append(sum_N(i) + sum_N(j))
print(min(ans))