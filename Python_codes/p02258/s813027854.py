n = int(raw_input())
R = []
R.append(int(raw_input()))
minv = R[0]
maxv = -1 * 10**9
for j in range(1,n):
    R.append(int(raw_input()))
    maxv = max(maxv,R[j]-minv)
    minv = min(minv,R[j])
print maxv