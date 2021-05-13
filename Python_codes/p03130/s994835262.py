n = 3
num_list = [list(map(int, input().split())) for _ in range(n)]
N = (sum(num_list, []))
N1 = N.count(1)
N2 = N.count(2)
N3 = N.count(3)
N4= N.count(4)
if N1 > 2 or N2 > 2 or N3 > 2 or N3 > 2 or N4 > 2:
    print('NO')
else:
    print('YES')
