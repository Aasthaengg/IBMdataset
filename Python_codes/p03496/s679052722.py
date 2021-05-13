def d_non_decreasing(N, A):
    from numpy import argmax, argmin
    a = A[:]
    a_max = max(a)
    a_argmax = argmax(a) + 1
    a_min = min(a)
    a_argmin = argmin(a) + 1  # +1するのは問題の数列が1-indexedだから
    ans = ''
    if abs(a_max) >= abs(a_min):
        ans += '{}\n'.format(2 * N - 1)  # 2N-1回の操作でソートされた数列になる
        for i in range(N):
            ans += '{} {}\n'.format(a_argmax, i + 1)  # 各数列に最大値を加算
        for i in range(1, N):
            ans += '{} {}\n'.format(i, i + 1)  # 累積和を取る
    else:
        ans += '{}\n'.format(2 * N - 1)
        for i in range(N):
            ans += '{} {}\n'.format(a_argmin, i + 1)  # 各数列に最小値を加算
        for i in range(N, 1, -1):
            ans += '{} {}\n'.format(i, i - 1)  # 累積和を取る
    ans=ans[:-1] #最後に改行が入ってしまうので、除く
    return ans
  
N = int(input())
A = [int(i) for i in input().split()]
print(d_non_decreasing(N, A))