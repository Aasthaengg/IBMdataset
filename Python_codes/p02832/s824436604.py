N = int(input())
A_n = list(map(int, input().split(' ')))

count = 0
last_i = 0
temp = 1
t = 0

if 1 not in set(A_n):
    print('-1')
else:
    for a in A_n:
        if a == temp:
            temp += 1
        else:
            count += 1
    print(count)