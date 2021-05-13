n = 0
w = input().lower()
while True:
    line = input()
    if line == 'END_OF_TEXT':
        break
    l=line.lower().split()
    n += l.count(w)
print(n)