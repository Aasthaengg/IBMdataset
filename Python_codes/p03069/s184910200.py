N = int(input())
S = list(input())
left = [0] * N
if S[0] == '#':
    left[0] += 1
for i in range(1,N):
    left[i] = left[i-1]
    if S[i] == '#':
        left[i] += 1
if left[-1] == 0:
    print(0)
    exit()

right = [0] * N
if S[-1] == '.':
    right[-1] += 1
for i in reversed(range(N-1)):
    right[i] = right[i+1]
    if S[i] == '.':
        right[i] += 1
if right[0] == 0:
    print(0)
    exit()
ans = min(left[-1],right[0])
for i in range(N):
    if S[i] == '#':
        ans = min(ans,left[i]-1 + right[i])
print(ans)
