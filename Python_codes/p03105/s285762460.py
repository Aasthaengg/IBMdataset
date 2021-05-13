a,b,c = map(int, input().split())
if b >= a * c:
    print(c)
else:
    sound = 0 if b < a else int(b / a)
    print(sound)