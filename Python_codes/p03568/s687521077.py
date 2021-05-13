from itertools import product
N = int(input())
A_list = list(map(int, input().split()))
ans = 0
cnt = 0
for i in A_list:
    if i % 2 == 0:
        cnt += 1
ans = 3**N - 2**cnt
print(ans)
