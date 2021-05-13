N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
print(X + sum([D//a if D%a==0 else (D//a)+1 for a in A]))
