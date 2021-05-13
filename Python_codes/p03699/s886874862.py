import sys
input = sys.stdin.readline


N = int(input())
s = [ int(input()) for _ in range(N)]
s= sorted(s)
sums = sum(s)
if sums %10 !=0:
    print(sums)
    exit()
else:
    for i in range(N):
        ans = sums - s[i]
        if ans % 10 != 0:
            print(ans)
            exit()
print(0)
