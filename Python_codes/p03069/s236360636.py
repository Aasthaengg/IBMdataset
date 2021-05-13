N = int(input())
S = input()

ldp = [0] * (N+1)
rdp = [0] * (N+1)

for i in range(N):
    if S[i] == "#":
        ldp[i+1] = ldp[i] + 1
    else:
        ldp[i+1] = ldp[i]

for i in range(N-1, -1, -1):
    if S[i] == ".":
        rdp[i] = rdp[i+1] + 1
    else:
        rdp[i] = rdp[i+1]

#print(ldp)
#print(rdp)
ans = 10 ** 9
for i in range(N+1):
    ans = min(ans, rdp[i]+ldp[i])

print(ans)