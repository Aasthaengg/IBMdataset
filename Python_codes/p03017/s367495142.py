import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,a,b,c,d = list(map(int, input().split()))
a -= 1
b -= 1
c -= 1
d -= 1
s = input()
if "##" in s[a:c+1]:
    ans = "No"
elif "##" in s[b:d+1]:
    ans = "No"
elif c>d and "..." not in s[b-1:d+2]:
    ans = "No"
else:
    ans = "Yes"
print(ans)