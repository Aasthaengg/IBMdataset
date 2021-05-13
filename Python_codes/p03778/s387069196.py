w, a, b = map(int, input().split())
s=0

if a<=b:
    s=b-(a+w)
else:
    s=a-(b+w)

if s<0:
    print(0)
else:
    print(s)