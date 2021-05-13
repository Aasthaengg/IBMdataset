NK = list(map(int,input().split()))
A = list(map(int,input().split()))
N = NK[0]
K = NK[1]

answer = (N - 1) // (K - 1)
remain = (N - 1) % (K - 1)
if remain > 0:
    answer = answer + 1
print(answer)