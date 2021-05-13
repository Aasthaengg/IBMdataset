ab=[list(map(int, input().split())) for _ in range(3)]
ab=sum(ab,[])
if ab.count(1)>=3 or ab.count(2)>=3 or ab.count(3)>=3 or ab.count(4)>=3:
    print('NO')
else:
    print('YES')

