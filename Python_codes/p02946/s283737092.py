import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


k,x = list(map(int, input().split()))
ans = list(range(x-k+1, x+k))
print(" ".join(map(str, ans)))