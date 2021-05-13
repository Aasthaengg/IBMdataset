n = int(input())
num_list = list(map(int, input().split()))

reversed = [1/i for i in num_list]
sum_under = 0
for j in reversed:
    sum_under += j

ans = 1/sum_under

print(ans)