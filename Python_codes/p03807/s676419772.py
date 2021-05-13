import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
a = list(map(int, input().split()))

odd = sum([num%2!=0 for num in a])
even = n-odd
if odd%2==0:
    print("YES")
else:
    print("NO")