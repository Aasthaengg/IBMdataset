import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b,c = map(int, input().split())
ans = min(a*b*(c%2), a*(b%2)*c, (a%2*b*c))
print(ans)