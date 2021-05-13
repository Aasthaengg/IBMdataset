H, W = map(int, input().split())
N = int(input())
A = list(map(int, input().split()))
L = sum([[i]*a for i, a in enumerate(A, 1)], [])
for i in range(H):
    inv = (-1)**(i&1)
    print(*L[i*W:(i+1)*W][::inv])