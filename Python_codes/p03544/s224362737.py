N = int(input())
R = [2, 1]
if N < 2:
    print(R[N])
    exit()
for i in range(2, N+1):
    R.append(R[i-1] + R[i-2])
print(R[N])