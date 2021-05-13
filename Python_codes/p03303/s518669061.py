import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**6)

s=input().rstrip()
w=int(input().rstrip())
a=""
for i in range(0,len(s),w):
    a+=s[i]
print(a)