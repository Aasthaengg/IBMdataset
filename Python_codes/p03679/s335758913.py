import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x,a,b = list(map(int, input().split()))
if x<-a+b:
    ans = "dangerous"
elif a>=b:
    ans = "delicious"
else:
    ans = "safe"
print(ans)