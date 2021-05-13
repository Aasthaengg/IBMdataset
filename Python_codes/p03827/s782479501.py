n = int(input())
s = input()

x = 0
xs = []
xs = [0] + xs
for i in range(n):
    if s[i] == "I":
        x += 1
    else:
        x -= 1
    xs.append(x)

print(max(xs))
