a,b = map(int, raw_input().split(' '))
print max(0, a - (b << 1))