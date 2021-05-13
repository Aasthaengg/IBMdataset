N, A, B = map(int, input().split())
rmax = min(A, B)
rmin = max(0, A+B-N)
print(rmax, rmin)
