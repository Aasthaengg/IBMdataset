n = int(input())
s = input()
c = 0
for i in range(n - 2):
    c = (c + 1) if s[i:i+3] == "ABC" else c
print(c)