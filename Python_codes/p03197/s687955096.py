N = int(input())
As = [int(input()) for _ in range(N)]

if all([a%2==0 for a in As]):
    print('second')
else:
    print('first')