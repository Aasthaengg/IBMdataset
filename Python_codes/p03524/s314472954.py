import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
s = input()
d = {"a":0, "b":0, "c": 0}
for c in s:
    d[c] += 1
if max(d.values()) - min(d.values())<=1:
    print("YES")
else:
    print("NO")