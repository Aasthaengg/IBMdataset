a=input()
b=input()
la,lb = len(a), len(b)
if a==b:
    print('No')
elif (la< lb and set(a)==set(b)):
    print('Yes')
else:
    sa = sorted(a)
    sb = sorted(b, reverse = True)
    if (sa[:lb] < sb):
        print('Yes')
    else:
        print('No')