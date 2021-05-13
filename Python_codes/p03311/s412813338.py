import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))
a = [(item-i-1) for i,item in enumerate(a)]
a.sort()
m = a[(n-1)//2]
ans = sum(abs(item-m) for item in a)
print(ans)