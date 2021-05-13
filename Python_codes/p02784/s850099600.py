import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


h, n = map(int, input().split())
a = list(map(int, input().split()))

if sum(a)>=h:
    print("Yes")
else:
    print("No")