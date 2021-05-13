n = raw_input()
ais = map(int, raw_input().split(' '))
print 'Yes' if sum(ais)>2*max(ais) else 'No'
