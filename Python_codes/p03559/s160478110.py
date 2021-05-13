N = int(input())

A = sorted(map(int, input().split()))
B = sorted(map(int, input().split()))
C = sorted(map(int, input().split()))

cur_l = 0
cur_r = 0
p = 0
for cur_mid in B:
    while cur_l < len(A):
        if A[cur_l] >= cur_mid:
            break
        cur_l += 1
    while cur_r < len(C):
        if cur_mid < C[cur_r]:
            break
        cur_r += 1
    p += cur_l * (len(C) - cur_r)

print(p)
