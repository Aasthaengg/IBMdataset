from itertools import accumulate

N, K = map(int, input().split())
A = map(int, input().split())


for _ in range(K):
    lamp = [0] * (N + 1)                    # imos法: 区間[l,r)　に要素を加算する操作を、lamp[l] += 1 と　lamp[r+1] -= 1　にすることで、
                                            # 情報の更新をO(1)で終わらせることができる。（愚直にやるとO(l-r) <= O(N)でアウト）
                                            # 右端を開にしているため、N+1 個の要素が必要。
    for i, a in enumerate(A):
        lamp[max(i-a,0)] += 1
        lamp[min(i+a+1,N)] -=1
    B = tuple(accumulate(lamp))[:-1]
    if B == A:
        break
    A = B


print(*A)