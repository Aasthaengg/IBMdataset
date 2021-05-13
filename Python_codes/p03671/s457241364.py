a, b, c = map(int, input().split())
ab=a+b
ac=a+c
bc=b+c

if ab < ac and ab < bc:
    print(ab)
elif ac < ab and ac < bc:
    print(ac)
elif bc < ab and bc < ac:
    print(bc)
else:
    print(ab)
