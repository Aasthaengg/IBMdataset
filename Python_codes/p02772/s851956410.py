N = int(input())
A = list(map(int, input().split()))
B = [x for x in A if x % 2 == 0 and x % 3 != 0 and x % 5 != 0]
if len(B) > 0:
    print('DENIED')
else:
    print('APPROVED')