import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

def turn(s,sa,sb,sc):
    if s == 'a':
        if len(sa) == 0:
            print('A')
            exit()
        trash = sa[-1]
        sa = sa[:-1:]
    elif s == 'b':
        if len(sb) == 0:
            print('B')
            exit()
        trash = sb[-1]
        sb = sb[:-1:]
    else:
        if len(sc) == 0:
            print('C')
            exit()
        trash = sc[-1]
        sc = sc[:-1:]
    return turn(trash,sa,sb,sc)

sa = readline().decode().rstrip()[::-1]
sb = readline().decode().rstrip()[::-1]
sc = readline().decode().rstrip()[::-1]

trash = sa[-1]
sa = sa[:-1:]

print(turn(trash,sa,sb,sc))