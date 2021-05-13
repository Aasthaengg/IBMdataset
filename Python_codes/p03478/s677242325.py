n, A, B = map(int, input().split())

sum_list = 0
for i in range(1, n+1):
    tmp = sum(list(map(int, str(i))))
    if A <= tmp and tmp <= B:
        sum_list += i
print(sum_list)