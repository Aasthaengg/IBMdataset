s = input().strip()
N = len(s)
C = {0:0,1:0}
for i in range(N):
    if s[i]=="g":
        C[0] += 1
    else:
        C[1] += 1
n = N//2
print(n-C[1])