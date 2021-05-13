import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
ans = 0
for i in range(1,n):
    if i**2>n:
        break
    if (n-i)%i==0 and (n-i)//i > i:
        ans += (n-i)//i
print(ans)