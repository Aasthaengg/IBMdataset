N = int(input())
A = tuple(map(int, input().split()))
assert len(A) == N

# 出席番号iの生徒が到着した時点でAi人が到着済み(i含む)
print(' '.join(list(map(str, sorted(range(1,N+1), key=lambda v:A[v-1])))))