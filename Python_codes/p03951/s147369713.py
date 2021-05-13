n = int(input())
s = input()
t = input()

r = n
for i in range(0, n):
    if s[i:] == t[:(n-i)]:
            break
    r += 1

print(r)
