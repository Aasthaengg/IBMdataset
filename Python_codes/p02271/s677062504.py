input()
s = {0}
for a in map(int,input().split()):
    for b in list(s):
        s.add(a+b)
input()
for e in map(int,input().split()):
    print('yes' if e in s else 'no')
