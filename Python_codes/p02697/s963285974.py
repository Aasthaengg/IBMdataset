N, M = map(int, input().split())
if M & 1:
    print(M, M+1)
m=M//2
for i in range(m):
    print(i+1, (-2-i)%N+1)
    print(i+m+1, 2*M-m-i)
