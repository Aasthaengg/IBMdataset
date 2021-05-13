N = int(input())
A_lst = [int(n) for n in input().split()]
odd = 0
even = 0
for A in A_lst:
    if A%2 == 0:
        even += 1
    else:
        odd += 1
print('YES') if odd%2 == 0 else print('NO')
