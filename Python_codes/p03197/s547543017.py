N = int(input())
As = [int(input()) for _ in range(N)]

for A in As:
    if A % 2:
        print('first')
        break
else:
    print('second')
