"""path = "/Users/hemmishinichi/PycharmProjects/AtCoder/ABC/ABC172/b08.txt"
with open(path) as f:
    l_strip = [s.strip() for s in f.readlines()]
    N, M, K = map(int, l_strip[0].split())
    A = [int(i) for i in l_strip[1].split()]
    B = [int(i) for i in l_strip[2].split()]
"""
N, M, K = map(int, input().split())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

time = 0
num_A = 0

for i in range(N):
    if time + A[i] > K:
        break
    else:
        time += A[i]
        num_A += 1
ans = num_A

i = 0
while i < M:
    #print(ans)
    while i < M and time + B[i] <= K:
        time += B[i]
        i += 1
    ans = max(num_A+i, ans)
    if i == M-1:
        break
    elif num_A > 0:
        num_A -= 1
        time -= A[num_A]
    else:
        break

print(ans)

