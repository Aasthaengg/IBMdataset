n,m=map(int,input().split())
part1 = n
part2 = m
if n*2 < m:
    part3 = (m-(n*2))//4
    print(n+part3)
elif n*2 > m:
    print(m//2)
