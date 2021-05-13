n = int(input())
s = list(input())
t = list(input())
count = 0
for i in range(n, 0, -1):
    if s[-i:] == t[:i]:
        count = i
        break
print(2 * n - count)