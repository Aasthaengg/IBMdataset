s1=input()
s2=input()

if s2==s1[::-1] and s1==s2[::-1]:
    print('YES')
else:
    print('NO')