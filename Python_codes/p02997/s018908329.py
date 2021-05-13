n, k = map(int,input().split())

# グラフ構築に必要な辺の本数は、最低n-1本
# 少なくとのn-1組の頂点対は距離1である
# 全頂点対の組み合わせの数 n*(n-1)/2 から n-1を引いたものが、作成可能な頂点対個数の最大値

if k > (n-1)*(n-2)/2:
    ans = -1
    print(ans)

# 頂点対の数が、(n-1)*(n-2)/2以下であるとき、n頂点からなるスターを考える
# ref. https://ja.wikipedia.org/wiki/%E3%82%B9%E3%82%BF%E3%83%BC_(%E3%82%B0%E3%83%A9%E3%83%95%E7%90%86%E8%AB%96)
# n頂点スターにおける、距離2の頂点対の組み合わせは(n-1)*(n-2)/2である
# スターの頂点以外の、ある2頂点をつなぐと、組み合わせは1つ減る
# (n-1)*(n-2)/2 - k 辺を用いて、頂点間を結ぶと、k個の距離2である頂点対が完成する
else:
    # 1を含まない(n-1)*(n-2)/2個の頂点対を用意しておく
    Cand = []
    for i in range(2, n):
        for j in range(i+1, n+1):
            Cand.append([str(i),str(j)])
    Ans = []
    for i in range(2,n+1):
        Ans.append([str(1),str(i)])
    for i in range(int((n-1)*(n-2)/2)-k):
        Ans.append(Cand[i])
    
    print(len(Ans))
    for i in range(len(Ans)):
        print(' '.join(Ans[i]))