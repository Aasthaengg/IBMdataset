from sys import stdin
def S(): return stdin.readline().rstrip()

t = S()

ans = ''
for i in range(len(t)):
    if t[i]!='?':
        ans += t[i]
    else:
        ans += 'D'
print(ans)