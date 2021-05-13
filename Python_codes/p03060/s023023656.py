N = int(input())
V = list(map(int, input().split()))
C = list(map(int, input().split()))
jewelry = [i-j for i, j in zip(V, C) if i-j > 0]
print(sum(jewelry))