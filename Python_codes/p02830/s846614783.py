N = int(input())
S ,T =input().split()
out = str()
for i in range(N):
    out += S[i] + T[i]

print(out)