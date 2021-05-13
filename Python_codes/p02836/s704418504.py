s = input()
n = int(len(s)/2)
x = 0
for i in range(n):
    if s[i] != s[-1-i]:
        x += 1
print(int(x))