X, K, D = map(int, input().split())

X = abs(X)
reach_or_before = X // D


if K <= reach_or_before:
    print(X - D * K)
else:
    #remaining jump
    remain = K - reach_or_before
    before_dist = X % D #(>0)
    after_dist = D - before_dist
    if remain % 2 == 0:
        print(before_dist)
    else:
        print(after_dist)
