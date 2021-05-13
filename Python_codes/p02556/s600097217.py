N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
tail = 0
head = float('inf')
for i in range(N):
    tail = max(tail, sum(A[i]))
    head = min(head, sum(A[i]))
ans_1 = tail - head

tmp_h, tmp_t = 0, 0
tail = A[i]
head = A[i]
for i in range(N):
    tail = A[i] if tmp_t < A[i][0]-A[i][1] else tail
    head = A[i] if tmp_h < A[i][1]-A[i][0] else head
    tmp_t = A[i][0]-A[i][1] if tmp_t < A[i][0]-A[i][1] else tmp_t
    tmp_h = A[i][1]-A[i][0] if tmp_h < A[i][1]-A[i][0] else tmp_h

ans_2 = abs(tail[0]-head[0]) + abs(tail[1]-head[1])
ans = max(ans_1, ans_2)
print(ans)