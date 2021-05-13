from collections import deque


N, M = map(int, input().split())
A = deque(sorted(list(map(int, input().split()))))
B = deque()

coupon = M
while coupon:
    try:
        if B:
            if A[-1] >= B[-1]:
                B.appendleft(A.pop() // 2)
            else:
                B.appendleft(B.pop() // 2)
        else:
            B.append(A.pop() // 2)
        coupon -= 1
    except IndexError:
        A, B = B, A


ans = sum(int(i) for i in A) + sum(int(i) for i in B)
print(ans)
