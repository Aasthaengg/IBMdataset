def peak():
    # 入力
    N, M = map(int, input().split())
    H = list(map(int, input().split()))
    A = list()
    B = list()
    for _ in range(M):
        dummy = list(map(int, input().split()))
        A.append(dummy[0])
        B.append(dummy[1])
    # 道がつながっている中で最大の展望台の高さを保存
    ovservatory_max_height = [0] * N
    for i in range(M):
        if H[B[i] - 1] > ovservatory_max_height[A[i] - 1]:
            ovservatory_max_height[A[i] - 1] = H[B[i] - 1]
        if H[A[i] - 1] > ovservatory_max_height[B[i] - 1]:
            ovservatory_max_height[B[i] - 1] = H[A[i] - 1]
    # つながっている展望台の最大長と比較
    is_good_list = list()
    for i in range(N):
        if H[i] > ovservatory_max_height[i] or ovservatory_max_height == 0:
            is_good_list.append(True)
        else:
            is_good_list.append(False)
    # 良い展望台の個数
    return is_good_list.count(True)    

result = peak()
print(result)