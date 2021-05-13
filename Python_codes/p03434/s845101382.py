N = int(input())
array = list(map(int, input().split()))
array.sort()
sum_1 = 0
sum_2 = 0

for i in range(N):
    if i % 2 == 0:
        sum_1 += array[-1]
        array.pop(-1)
        
    else:
        sum_2 += array[-1]
        array.pop(-1)
print(sum_1 - sum_2)
