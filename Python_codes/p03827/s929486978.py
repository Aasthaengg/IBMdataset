n = int(input())
s = input()

x = 0
x_max = 0

for i in s:
    x = x+1 if i=='I' else x-1
    x_max = max(x, x_max)

print(x_max)


