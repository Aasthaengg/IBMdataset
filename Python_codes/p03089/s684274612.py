import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
b = list(map(int, input().split()))
ans = []
for i in range(n):
    target = None
    for j in range(n-i):
        if int(b[j])==j+1:
            target = j
    if target is None:
        ans = -1
        break
    ans.append(target+1)
    b = b[:target] + b[target+1:]
else:
    ans = "\n".join(map(str, ans[::-1]))
print(ans)