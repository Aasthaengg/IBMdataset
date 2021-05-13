import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


a,b,c,d = map(int, input().split())
v1 = c//b + int(c%b!=0)
v2 = a//d + int(a%d!=0)
if v1<=v2:
    ans = "Yes"
else:
    ans = "No"
print(ans)