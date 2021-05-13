l, r, d = map(int, input().split())

if l % d == 0:
    a = l // d
    b = r // d
    print(b-a+1)
else:
    a = l // d
    b = r // d
    print(b-a)