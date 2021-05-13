N = int(input())
P = [int(input()) for i in range(N)]
print(max(P)//2 + sum(sorted(P)[0:(N-1)]))