 
s=input()
k=15-len(s)
if s.count('o')+k >= 8:
    print('YES')
else:
    print('NO')