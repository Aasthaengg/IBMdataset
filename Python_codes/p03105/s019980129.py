a,b,c = map(int, input().split())

if a <= b:
    if c >= int(b/a):
        print(int(b/a))
    else:
        print(c)
else:
    print(0)