import sys
input = sys.stdin.readline

n = int(input())
a = int(input())

n %= 500
ans = "Yes" if n <= a else "No"
print(ans)




