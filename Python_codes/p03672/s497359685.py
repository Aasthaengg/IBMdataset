s = input()
n = len(s)
if n%2==0:
    n -= 1
    s = s[:-1]
while n%2!=0 or s[:n//2]!=s[n//2:]:
    n -= 1
    s = s[:-1]
print(n)