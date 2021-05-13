N = input()
leftt = N[:3]
right = N[1:]

if (len(set(leftt)) == 1 or len(set(right)) == 1):
    print('Yes')
else:
    print('No')