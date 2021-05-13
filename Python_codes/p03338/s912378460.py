# input
N = int(input())
S = input()

# check
max = 0
for i in range(N):
    A, B = set(S[:i + 1]), set(S[i + 1:])
    union_cnt = len(A & B)
    
    if max < union_cnt:
        max = union_cnt

print(max)