import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
n = len(s)
nx = []
for i in range(n):
    if s[i]=="R":
        nx.append(i+1)
    else:
        nx.append(i-1)
v = 1
while v<10*n:
    nx = [nx[i] for i in nx]
    v *= 2
ans = [0]*n
for num in nx:
    ans[num] += 1
write(" ".join(map(str, ans)))