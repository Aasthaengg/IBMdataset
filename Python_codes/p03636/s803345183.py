import sys
s = list(sys.stdin.readline().rstrip("\n"))
i = s.pop(0)
f = s.pop(-1)
print(i+str(len(s))+f)