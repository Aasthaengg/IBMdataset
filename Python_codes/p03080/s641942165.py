n = int(input())
s = input()
m = 0
for i in range(n):
    if s[i] == 'R':
        m = m + 1
if m > n // 2 : print("Yes")
else : print("No")