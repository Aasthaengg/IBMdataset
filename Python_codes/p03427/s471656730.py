# mv = 0
# for i in range(10**2-1, 10**3+1):
#     ns = 0
#     si = str(i)
#     n = len(si)
#     for j in range(n):
#         ns += int(si[j])
#     mv = max(mv, ns)
#     print(i, mv)

N = input()
ok = True
for i in range(len(N)-1):
    if N[i+1] != '9':
        ok = False

if len(N) == 1:
    print(int(N))
    exit()
ans = 0
if ok:
    for i in range(len(N)):
        ans += int(N[i])
else:
    if N[0] == '1':
        for i in range(len(N)-1):
            ans += 9
    else:
        ans += int(N[0]) - 1
        for i in range(len(N)-1):
            ans += 9

print(ans)