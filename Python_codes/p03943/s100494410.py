a,b,c = list(map(int,input().split()))
d = [a,b,c]
d.sort()
print('Yes' if d[0]+d[1]==d[2] else 'No')