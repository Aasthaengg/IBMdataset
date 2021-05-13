s = input()
p = sum(1 for i in s if i == 'p')
l = len(s)
print(l // 2 - p)