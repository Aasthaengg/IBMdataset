a,b = map(int, raw_input().split(' '))
print max((a<<1) - 1, (b<<1)-1, a + b)