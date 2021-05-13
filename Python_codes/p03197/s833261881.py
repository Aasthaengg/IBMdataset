N = int(input())
odd = 0
for i in range(N):
    a = int(input())
    if a % 2 == 1:
        odd += 1
if odd:
    print('first')
else:
    print('second')
