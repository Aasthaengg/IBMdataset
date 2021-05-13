n = int(input())
n_s = str(n)
m = 0
for i in range(len(n_s)):
    m += int(n_s[i])
    m = m % 9

if m == 0:
    print("Yes")
else:
    print("No")
