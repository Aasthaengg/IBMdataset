N = int(input())
divisions = []
for i in range(1, int(N**(1/2)+1)):
    if N % i == 0:
        divisions.append(i)
        divisions.append(N//i)
ans = 0
for d in divisions:
    if d == 1:
        continue
    if N // (d-1) == N % (d-1):
        ans += d-1
print(ans)
