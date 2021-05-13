N = int(input())
a = sorted(map(int, input().split(' ')), reverse=True)

sum_value = 0
for n in range(1,N+1):
    num = a[2*n-1]
    sum_value += num

print(sum_value)