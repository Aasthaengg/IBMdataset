N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
E = 0 #食べた総数

for a in A:
    E += int((D-1) / a) + 1
print(E+X)