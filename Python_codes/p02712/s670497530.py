N = int(input())
N3 = N//3
N5 = N//5
N15 = N//15

ans = N*(N+1)/2 - 3*N3*(N3+1)/2 -5*N5*(N5+1)/2 + 15*N15*(N15+1)/2

print(int(ans))