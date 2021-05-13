l = [chr(i).upper() for i in range(ord('a'), ord('a')+6)]
a, b = (l.index(i) for i in input().split())
print('>' if a>b else '<' if a<b else '=')