N = int(input())
P = [int(input()) for i in range(N)]

print(int(max(P) * 0.5 + sum(P) - max(P)))