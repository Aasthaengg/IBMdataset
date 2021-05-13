k,x = map(int, raw_input().split(' '))
ee = range(max(x - k+1,-1000000), min(x + k,1000000))
print ' '.join(map(str,ee))