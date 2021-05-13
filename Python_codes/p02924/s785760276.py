#139D

#ここから試験用コード
'''
import itertools

for N in range(1,13):
    l = [i for i in range(1,N+1)]

    ans = 0
    ans_permutation = list()

    for permutation in itertools.permutations(l, N):
        temp_ans = 0
        permutation = [0] + list(permutation)
        for i in range(1,N+1):
            temp_ans += i%permutation[i]

        if ans <= temp_ans:
            if ans < temp_ans:
                ans_permutation = list()
            ans = temp_ans    
            ans_permutation.append(list(permutation)[1:])

    print(N,ans,ans_permutation)
    
#試験用コードの結果
# 1  0 [[1]]
# 2  1 [[2, 1]]
# 3  3 [[1, 3, 2], [2, 3, 1]]
# 4  6 [[2, 3, 4, 1]]
# 5 10 [[1, 3, 4, 5, 2], [2, 1, 4, 5, 3], [2, 3, 4, 5, 1]]
# 6 15 [[2, 3, 4, 5, 6, 1]]
# 7 21 [[1, 3, 2, 5, 6, 7, 4], [1, 3, 4, 5, 6, 7, 2], [2, 3, 1, 5, 6, 7, 4], [2, 3, 4, 5, 6, 7, 1]]
# 8 28 [[2, 1, 4, 5, 6, 7, 8, 3], [2, 3, 4, 5, 6, 7, 8, 1]]
# 9 36 [[1, 3, 4, 5, 6, 7, 8, 9, 2], [2, 3, 4, 1, 6, 7, 8, 9, 5], [2, 3, 4, 5, 6, 7, 8, 9, 1]]
#10 45 [[2, 3, 4, 5, 6, 7, 8, 9, 10, 1]]

#いずれにも最初は2,3...、最後は1となるパターンがある
#上記パターン時は ((N-1)+1)*(N-1)/2 が答え。
'''
N = int(input())
print(N*(N-1)//2)
