import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline

s=input().rstrip()
n=len(s)
t="keyence"
for i in range(n):
    for j in range(i,n):
        if s[:i]+s[j:]==t:
            print("YES")
            exit()
print("NO")