c1=input()
c2=input()

print('YES' if c1==c2[::-1] and c2==c1[::-1] else 'NO')