import math

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# 総和が等しくなることが必要条件なので、操作回数は sum(B) - sum(A)
def f():
    a_ctr = 0
    b_ctr = 0
    handle = sum(B) - sum(A)
    if handle < 0: return 0 # Aの総和が大きければ無理
    # A に足していく
    for i in range(N):
        if A[i] == B[i]:
            pass
        if A[i] > B[i]: 
            b_ctr += A[i] - B[i]
        else: 
            a_ctr += math.ceil((B[i] - A[i]) / 2)
            if (B[i] - A[i]) % 2 == 1: b_ctr += 1
    # print(a_ctr, b_ctr, handle)
    if a_ctr == b_ctr == handle: return 1
    if a_ctr < handle and b_ctr < handle and (handle - a_ctr) * 2 == handle - b_ctr: return 1
    return 0

if f():
    print("Yes")
else:
    print("No")