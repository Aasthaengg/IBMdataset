S = int(input())
Mod = 10**9+7
a=[1]
for i in range(S):
    i += 1
    if i > 2:
        a.append((a[-1] + a[-3])%Mod)
    else:
        a.append(0)
print(a[S])
