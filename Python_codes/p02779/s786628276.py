N = int(input())
A = list(input().split())
B = set(A)
if len(A) == len(B):
    ans = "YES"
else:
    ans = "NO"
print(ans)
