w = input().lower()
t = []
s = input()
while (s != 'END_OF_TEXT') :
    t += s.lower().split()
    s = input()
print(len([x for x in t if x == w]))
