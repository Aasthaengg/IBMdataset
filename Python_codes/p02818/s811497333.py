A, B, K = list(map(int, input().split(' ')))
# print(str(A-k) + ' ' + str(K-A-B))
if A + B <= K:
    print('0 0')
elif A >= K:
    print(str(A-K) + ' ' + str(B))
else:
    print('0 ' + str(A+B-K))
