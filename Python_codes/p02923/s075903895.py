N = int(input())
H = list(map(int,input().split()))
m = 0
s = 0
M = []
for i in range(N-1):
    if H[i] >= H[i+1]:
        s += 1
        m = max(m,s)
    else:
        m = max(m,s)
        s = 0
    # print(s)
print(m)