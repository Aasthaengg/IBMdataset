n = int(input())
s = input()
if n % 2 != 0:
    print('No')
    exit()
if s[:n//2] == s[n//2:n]:
    print('Yes')
else:
    print('No')
