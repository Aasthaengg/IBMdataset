N = int(input())
a = [int(input())%2 for i in range(N)]
if 1 not in a:
    print('second')
else:
    print('first')