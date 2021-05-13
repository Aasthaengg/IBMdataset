w = str(input())
c=[]
while True:
    s = str(input())
    if (s == 'END_OF_TEXT'):
        break
    c += s.lower().split()
print(c.count(w))

