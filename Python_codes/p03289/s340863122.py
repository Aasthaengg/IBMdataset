import sys
s = input()

if s[0] != 'A':
    print("WA") 
    sys.exit()
if s[2:-1].count("C")!=1:
    print("WA")
    sys.exit()

# Aが頭にあってCは一つしかない
for i,c in enumerate(s):
    if i != 0 and i!=s[2:-1].index("C")+2:
        if ord(c) <= 90:
            print("WA")
            sys.exit()

print("AC")

