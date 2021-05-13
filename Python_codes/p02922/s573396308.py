import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b = list(map(int, input().split()))
ans = (b-1) // (a-1) + int((b-1)%(a-1)!=0)
print(ans)