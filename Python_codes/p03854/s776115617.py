s = str(input())
a = ['dream', 'dreamer', 'erase', 'eraser']

f = True
while f:
    os = s
    for i in a:
        if s.endswith(i):
            s = s[:-len(i)]
            if len(s) == 0:
                print("YES")
                f = False
    if len(os) == len(s):
        print("NO")
        f = False
