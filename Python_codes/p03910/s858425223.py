import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")



n = int(input())
i = 1
s = 1
ss = set([1])
while s<n:
    i += 1
    s += i
    ss.add(i)
    
if s>n:
    ss.remove(s-n)
write("\n".join(map(str, ss)))