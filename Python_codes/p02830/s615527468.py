import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s,t = input().split()
ans = "".join(item[0]+item[1] for item in  zip(s,t))
print(ans)