s = input()
z = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
s_alpha = [[] for _ in range(26)]
z_alpha = [[] for _ in range(26)]
for num, i in enumerate(s):
    pos = alpha.index(i)
    s_alpha[pos].append(num)
for num, i in enumerate(z):
    pos = alpha.index(i)
    z_alpha[pos].append(num)
s_alpha.sort()
z_alpha.sort()
if s_alpha == z_alpha:
    print("Yes")
else:
    print("No")
