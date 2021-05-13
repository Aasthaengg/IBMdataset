N = int(input())
A = input()

r_cnt = A.count('R')

ans = 0
for i in range(r_cnt):
    if A[i] != 'R':
        ans += 1

print(ans)