n = int(input())
c = input()
nr = c.count('R')
nr2 = c[:nr].count('R')
print(nr - nr2)