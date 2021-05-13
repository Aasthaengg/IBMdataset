n = int(input())
a_1 = list(map(int, input().split()))
a_2 = list(map(int, input().split()))

sum_a_1 = [0]
sum_a_2 = [0]
for i in range(n):
    sum_a_1.append(sum_a_1[-1] + a_1[i])
    sum_a_2.append(sum_a_2[-1] + a_2[n-i-1])
    
res = 0
for i in range(n):
    res = max(res, sum_a_1[i+1] + sum_a_2[n-i])

print(res)