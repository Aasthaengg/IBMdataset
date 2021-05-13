a,b,c = map(int,input().split())
poor = False
if a == b and a != c:
    poor = True
elif c == b and c != a:
    poor = True
elif a == c and a != b:
    poor = True
if poor:
    print('Yes')
else:
    print('No')
