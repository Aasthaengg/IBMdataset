import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n = int(input())
s = input()
if n%2==1:
    ans = "No"
elif s[:n//2]==s[n//2:]:
    ans = "Yes"
else:
    ans = "No"
print(ans)