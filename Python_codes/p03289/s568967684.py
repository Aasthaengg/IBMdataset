S = input()

# S = 'AaCa'
# print( S[1], S[-1], S[3:-2])

b = True
b = b and (S[0]=='A')
b = b and ( S[2:-1].count('C')==1 )

b = b and ( 'a' <= S[1] <= 'z')
b = b and ( 'a' <= S[-1] <= 'z')

for c in S[3:]:
  b = b and ( ('a' <= c <= 'z') or (c=='C') )

print( "AC" if b else "WA" )
