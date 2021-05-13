N=int(input())
A=list(map(int,input().split()))
B=[abs(_-(sum(A)/N)) for _ in A]
for _ in range(N):
    if B[_]==min(B):
        print(_)
        exit()