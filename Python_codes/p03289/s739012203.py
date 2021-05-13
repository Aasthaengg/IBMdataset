s = input()

if not s[0] == "A":
    print ("WA")
    exit ()

if not list(s[2:-1]).count("C") == 1:
    print ("WA")
    exit ()

s = (s.replace('A','')).replace('C','')

if s.islower():
    print ("AC")
else:
    print ("WA")
