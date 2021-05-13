h,w = map(int, raw_input().split())
m = [raw_input() for _ in range(h)]
for i in range(2*h): print ''.join([m[(i)/2][j] for j in range(w)]) 