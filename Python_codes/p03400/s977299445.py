N = int(input())
D,X = map(int,input().split())
A = [int(input()) for n in range(N)]
print(X+sum([-(-D//a) for a in A]))