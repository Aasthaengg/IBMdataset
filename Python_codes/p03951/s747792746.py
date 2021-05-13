n=int(input())
s=input()
t=input()
match = 0

for i in range(n):
    if s[i:] == t[:n-i]:
        match = n-i
        break

print(2*n-match)