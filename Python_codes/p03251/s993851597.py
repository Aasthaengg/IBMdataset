n,m,X,Y = map(int, raw_input().split(' '))
xis = map(int,raw_input().split(' '))
xis.sort()
yis = map(int,raw_input().split(' '))
yis.sort()

aa = [xis[n - 1], yis[-m]]
aa[0] = max(aa[0], X)
aa[1] = min(aa[1], Y)
print 'No War' if aa[0]<aa[1] else 'War'