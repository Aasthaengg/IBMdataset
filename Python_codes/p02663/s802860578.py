h1,m1,h2,m2,k = map(int,input().split())
H_min = (h2-h1)*60
M_min = m2-m1
time = H_min + M_min
ans = time - k
print(ans)