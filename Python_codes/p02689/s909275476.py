N, M = map(int, input().split())
H_list = list(map(int, input().split()))
H = [1 for i in range(N)]
for i in range(M):
  A, B = map(int, input().split())
  if H_list[A-1] >= H_list[B-1]:
    H[B-1] = 0
  if H_list[A-1] <= H_list[B-1]:
    H[A-1] = 0

print(sum(H))