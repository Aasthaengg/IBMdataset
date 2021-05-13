s = input()
rs = s[::-1]
x = s.index('A')
y = rs.index('Z')
print(len(s)-y-x)
