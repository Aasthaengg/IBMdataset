import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)+1
v1 = [None]*n
v2 = [None]*n
v1[0] = 0
v2[-1] = 0
v = 0
for i,c in enumerate(s):
    if c=="<":
        v += 1
    else:
        v = 0
    v1[i+1] = v
v = 0
for i,c in enumerate(s[::-1]):
    if c==">":
        v += 1
    else:
        v = 0
    v2[n-2-i] = v
ans = [max(v1[i], v2[i]) for i in range(n)]
print(sum(ans))