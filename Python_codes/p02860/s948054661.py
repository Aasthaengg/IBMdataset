n = int(input())
s = input()
if n%2==1:
    print('No')
    exit(0)

if s[:n//2] == s[-n//2:]:
    print('Yes')
else:
    print('No')