c=list(map(int, input().split()))

if sum(c) <= 21:
    print('win')
else:
    print('bust')