N = input()
n = len(N)
ok = 1
for i in range(n):
    if N[i] == N[n-i-1]:
        continue
    ok = 0
    break
if ok:
    print("Yes")
else:
    print("No")
