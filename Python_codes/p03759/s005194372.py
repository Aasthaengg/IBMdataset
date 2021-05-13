import sys
input = sys.stdin.readline
a,b,c=map(int,input().split())
print("YES" if b-a==c-b else "NO")
