from sys import stdin
s = (stdin.readline().rstrip())
g = s.count("g")
p = s.count("p")
c = len(s)//2
print(c-p)    