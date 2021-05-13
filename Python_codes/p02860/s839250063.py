n = int(input())
s = input()
if n % 2 == 1:
    print('No')
else:
    mid = int(n/2)
    if s[0:mid] == s[mid:n]:
        print('Yes')
    else:
        print('No')