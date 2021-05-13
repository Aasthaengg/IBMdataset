import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h,w,a,b = map(int, input().split())
ans = [None for _ in range(h)]
for i in range(h):
    if i<b:
        ans[i] = [0]*a + [1]*(w-a)
    else:
        ans[i] = [1]*a + [0]*(w-a)
write("\n".join("".join(map(str, item)) for item in ans))