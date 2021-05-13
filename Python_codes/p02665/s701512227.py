from sys import stdin, stdout
n = int(stdin.readline())
nmleaves = list(map(int, stdin.readline().strip().split()))

if nmleaves[0]:
   if n == 0 and nmleaves[0] == 1:
      print(1)
   else:
      print(-1)
   exit()

# pref[i]: sum(nmleaves[i:]), i.e., the number of leaves at or below level i.
pref = [0]*(n+1)
totsum = sum(nmleaves)
pref[0] = totsum
t = 0
for i in range(1, n+1):
    t += nmleaves[i-1]
    pref[i]  = totsum - t

prev_nl = 1
ans = 1
for lev in range(1, n+1):
    nodes = min(prev_nl*2, pref[lev])
    ans += nodes
    prev_nl = nodes - nmleaves[lev]
    if prev_nl < 0:
        print(-1)
        exit()
    elif prev_nl == 0 and lev+1<n+1 and pref[lev + 1]>0:
        print(-1)
        exit()
print(ans)