n = int(input())
s = input()
t = input()

for i in range(n, 2*n+1):
    if s[n - (2*n-i):] == t[:2*n-i]:
        print(i)
        exit()

print(2*n)
