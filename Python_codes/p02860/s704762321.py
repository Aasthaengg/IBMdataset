n = int(input())
s = input()
if n%2==0:
    print('Yes' if s[:int(n/2)]==s[int(n/2):] else 'No')
else:
    print('No')