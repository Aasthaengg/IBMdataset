N = int(input())

# i を P[i] = i+1 で割る (i=1,..., N-1)が最大

res = N * (N-1) // 2

print(res)