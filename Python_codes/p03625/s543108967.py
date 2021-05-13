from collections import Counter

N = int(input())
A = list(input().split())
A = [int(A[i])for i in range(N)]
A_count = list(Counter(A).most_common())

rectangle = sorted([A_count[i][0] for i in range(len(A_count)) if A_count[i][1] >= 2],reverse=True)
square = sorted([A_count[i][0] for i in range(len(A_count)) if A_count[i][1] >= 4], reverse=True)

S_rec = (rectangle[0] * rectangle[1] if len(rectangle) >= 2 else 0)
S_squ = (square[0] ** 2 if len(square) >= 1 else 0)

print(max(S_rec, S_squ))
