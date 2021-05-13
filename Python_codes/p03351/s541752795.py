import sys

def aa097():
    a,b,c,d = list(map(int, input().split()))
    if abs(a-c) <= d:
        print('Yes')
        sys.exit()

    if abs(a-b) <= d and abs(b-c) <= d:
        print('Yes')
        sys.exit()

    print('No')

aa097()
