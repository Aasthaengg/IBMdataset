n = int(input())
a_lis = list(map(int, input().split()))
a_sum = sum(a_lis)
a_avg = a_sum / n
minimum = 1000
ans = 0
for i in a_lis:
    n = abs(a_avg - i)
    if n < minimum:
        minimum = n
        ans = i
print(a_lis.index(ans))