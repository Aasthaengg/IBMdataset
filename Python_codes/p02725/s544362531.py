def distance_between_houses(d1, d2=0):
    """
    2点の基準値からの距離を引数に2点間の距離を求める。
    引数：d1 : 家１の基準値からの距離
    　　　d2 : 家２の基準値からの距離
    戻り値：2点間の距離
    """
    return d2 - d1

def traveling_salesman_around_lake():
    # 入力
    K, N = map(int, input().split())
    A = list(map(int, input().split()))
    # 家と家との距離
    distances = list()
    for i in range(N):
        if i < N-1 :
            distances.append(distance_between_houses(A[i], A[i+1]))
        # 基準値から最も遠い家と最も近い家の距離
        else:
            distances.append(distance_between_houses(A[i], A[0]+K))
    # 最も遠い距離をリストから除外
    max_value_ind = distances.index(max(distances))
    distances.pop(max_value_ind)
    # リストを全合計
    return sum(distances)

result = traveling_salesman_around_lake()
print(result)