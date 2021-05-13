from math import ceil
N = int(input())
A_list = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(N):
    if A_list[A_list[i]-1]-1 == i:
        ans += 1
print(ans//2)