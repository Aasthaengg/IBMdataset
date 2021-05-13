N = int(input())
P = list(map(int,input().split()))
P_sort = sorted(P)
counter = 0
for p,p_sort in zip(P,P_sort):
    if p != p_sort:
        counter += 1
if counter == 2 or counter == 0:
    print('YES')
else:
    print('NO')