n = int(input())
s = input()
t = input()
p = n * 2

for i in range(n):
    if t[0:i+1] in s:
        p -= 1
    else:
        break

print(p)