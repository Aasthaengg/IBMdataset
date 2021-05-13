n = int(input())
LIST=[list(map(int,input().split()))for i in range(n)]

plus=[i[0]+i[1]for i in LIST]
minus=[i[0]-i[1]for i in LIST]

d_plus=max(plus)-min(plus)
d_minus=max(minus)-min(minus)

print(max(d_plus, d_minus))