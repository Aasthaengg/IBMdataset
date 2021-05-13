s = str(input())
a = ['A','T','G','C']
b = []
c = 0
for i in s:
    if i in a:
        c += 1
    else:
        b += [c]
        c = 0
b += [c]
if b == []:
    print(len(s))
else:
    print(max(b))