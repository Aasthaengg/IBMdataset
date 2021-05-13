def f(a,b): return a <= 8 and b <= 8
a,b = map(int, raw_input().split())
print 'Yay!' if f(a,b) else ':('