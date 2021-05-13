def d_decrease(SIZE=50):
    K = int(input())

    # q 回数列全体を +1 し，r 回のシミュレーションを行う．
    # ans[r] を +SIZE し，その他の要素を -1 する．まとめて書くと以下の通り
    q, r = divmod(K, SIZE)
    ans = list(map(lambda x: x + q - r, range(SIZE)))
    for i in range(r):
        ans[i] += SIZE + 1
    return '{}\n{}'.format(SIZE, ' '.join(map(str, ans)))

print(d_decrease())