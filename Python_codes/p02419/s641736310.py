w = input().lower()
r = []
s = input()
while (s != "END_OF_TEXT"):
    r += s.lower().split()
    s = input()
print(len([x for x in r if x == w]))
