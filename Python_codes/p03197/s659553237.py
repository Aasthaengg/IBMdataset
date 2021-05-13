n=int(input())
A=[int(input()) for _ in range(n)]

if all([a%2==0 for a in A]):
    print('second')
else:
    print('first')