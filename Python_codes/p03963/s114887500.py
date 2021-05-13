s = input()
slist = s.split(' ')
n = int(slist[0])
k = int(slist[1])

print(k * ((k - 1) ** (n - 1)))