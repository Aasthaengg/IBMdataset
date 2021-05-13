s=input()


s=s.replace('eraser','')
s=s.replace('erase','')
s=s.replace('dreamer','')
s=s.replace('dream','')

print('YES') if len(s)==0 else print('NO')
