N, A, B = map(int,input().split())
h = []
for _ in range(N):
    h.append(int(input()))
 
def solve(n):
    cnt = 0
    for i in h:
        i -= B * n
        cnt += max((i - 1) // (A - B) + 1, 0)
    return cnt <= n
 
left = 0
right = 10 ** 9

while left + 1 < right:
    mid = (left + right) // 2
    if solve(mid):
        right = mid
    else:
        left = mid
 
print(right)