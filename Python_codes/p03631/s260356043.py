import sys
input = sys.stdin.readline

n = input().rstrip("\r\n")
ans = "Yes" if n[0]==n[2] else "No"
print(ans)