n = int(input())
d, x = (int(i) for i in input().split())
A = [None] * n
for i in range(n):
    A[i] = int(input())
    
eated_num = 0
for a in A:
    i = 0
    while True:
        eat_date = i*a + 1
        if eat_date <= d:
            eated_num += 1
            i += 1
        else:
            break
print(eated_num + x)