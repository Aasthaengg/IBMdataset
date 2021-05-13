S = list(input())
w = int(input())
N = len(S)
out = []
for i in range(N):
    if i%w==0:
        out.append(S[i])
print("".join(out))
