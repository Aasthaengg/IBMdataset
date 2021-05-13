import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


s = input()
for i in range(len(s)):
    if (i%2==0 and s[i]=="L") or (i%2==1 and s[i]=="R"):
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)