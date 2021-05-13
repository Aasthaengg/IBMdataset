N = int(input())
for i in range(N,1000):
    S = str(i)
    if S[0] == S[1] and S[1] == S[2]:
        out = i
        break
print(out)
