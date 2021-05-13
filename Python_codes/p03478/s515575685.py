N , A , B = map(int, input().split())

L = [i for i in range(1, N+1)]
M = []
def digitSum(n):
    # 数値を文字列に変換
    s = str(n)
    # １文字ずつ数値化し配列にする。
    array = list(map(int, s))
    # 合計値を返す
    return sum(array)

for i in range(N):
    if digitSum(L[i]) >= A and digitSum(L[i]) <= B:
        M.append(L[i])
        

        
print(sum(M))