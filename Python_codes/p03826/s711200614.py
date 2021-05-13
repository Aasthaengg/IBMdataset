#ABC052A
a,b,c,d = map(int,input().split())
if (a * b == c * d):
    print(a * b)
else:
    print(max(int(a * b),(c * d)))
