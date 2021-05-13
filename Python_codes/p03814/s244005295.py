s = list(input())
Z_place = 0
A_place = s.index('A')

for i in s[:A_place:-1]:
     if i != 'Z':
        Z_place += 1
     else:
         break

print(len(s) - (A_place + Z_place))