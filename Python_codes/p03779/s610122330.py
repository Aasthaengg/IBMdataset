import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x = int(input())
k = 0
while k*(k+1)//2 < x:
    k += 1
ans = k
print(ans)