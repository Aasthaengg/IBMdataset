s=input()
if all(s.count(i)%2==0 for i in set(s)):
    print('Yes')

else:
    print('No')
