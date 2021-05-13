import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


# inputna
n = int(input())
a = list(map(int, input().split()))
ans = 1/sum((1/num) for num in a)
print(ans)