def bin_tree( pri , li_pri , len_li ):
    #pri: どこに入れていいかわからない値段
    #li_pri: 値段のリスト(昇順)
    #len_li: リストの長さ
    lo = 0
    hi = len_li - 1
    while hi - lo > 1:
        mid = lo + (hi - lo) // 2
        guess = li_pri[mid]
        if guess >= pri:
            hi = mid
        else:
            lo = mid
    return lo

I = input().split()
N = int(I[0])
M = int(I[1])
# N: 品物の数
# M: 割引券の数
# A: 品物の値段行列
A = list(map(int , input().split()))
A.sort()

while M > 0:
    M -= 1
    pri = A.pop( N - 1 )
    pri = pri // 2
    if len(A) == 0:
        ans = 0
    elif (pri < A[0] ):
        ans = 0
    else:
        ans = bin_tree( pri , A , N - 1 ) + 1
    # ans: pri以上となる値段のうち最小のインデックス
    A[ans:ans] = [pri]    

F_pri = 0
for i in range(N):
    F_pri += A[i]
print(F_pri)