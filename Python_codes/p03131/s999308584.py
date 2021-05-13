import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


k,a,b = list(map(int, input().split()))
c = 1
if b<=a+2:
    ans = c + k
else:
    if k<=(a-c):
        ans = c + k
    else:
        c = a
        k -= (a-1)
        ans = c + (b-a)*(k//2)
        if k%2==1:
            ans += 1
print(ans)