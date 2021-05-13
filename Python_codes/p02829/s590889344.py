import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a = int(input())
b = int(input())
s = set(range(1,4))
s.remove(a)
s.remove(b)
print(s.pop())