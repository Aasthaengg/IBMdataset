
N = int(input())

S = input()

ans = float("inf")

lb = 0
rw = 0

for i in range(N):
    if S[i] == ".":
        rw += 1

for i in range(N+1):

    ans = min(ans , lb + rw)

    if i == N:
        break

    if S[i] == "#":
        lb += 1
    else:
        rw -= 1

print (ans)
        
