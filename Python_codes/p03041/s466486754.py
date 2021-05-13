from sys import stdin
def S(): return stdin.readline().rstrip()
def LI(): return list(map(int,stdin.readline().rstrip().split()))

tmp = LI()
n,k = [tmp.pop(0) for _ in range(2)]
s = list(S())
k -= 1
l = {'A':'a', 'B':'b', 'C':'c'}

s[k] = l[s[k]]

ans = ''

for i in range(n):
    ans += s[i]

print(ans)