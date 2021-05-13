s = list(map(int, input().split()))
d=abs(s[2]-s[1])
if d>s[0]:
    print(d-s[0])
else:
    print(0)