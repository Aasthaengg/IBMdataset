n = int(input())
s = input()
if n%2 == 1:
    print('No')
else:
    s1, s2 = s[:n//2], s[n//2:]
    if s1 == s2:
        print('Yes')
    else:
        print('No')