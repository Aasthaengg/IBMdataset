N = int(input())
A = list(map(int,input().split()))
A2 = [i%2 for i in A]
ac = A2.count(1)
if ac%2:
    print('NO')
else:
    print('YES')