s = input()
n = len(s)
max_p = n // 2
numg = s.count("g")
nump = s.count("p")
print(max_p - nump)