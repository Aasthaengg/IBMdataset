line = raw_input()
line = line.split(" ")
N,H,W = line
N = int(N)
H = int(H)
W = int(W)
ans = 0

for i in range(N):
    line = raw_input()
    line = line.split(" ")
    hi,wi = line
    hi = int(hi)
    wi = int(wi)

    if hi >= H and wi >= W:
        ans += 1
        
print ans