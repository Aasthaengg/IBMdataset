s = input()
l = list(s)

a = l.count('0')
b = l.count('1')

ans = 2 * min(a, b)
print(ans)