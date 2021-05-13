a,b,c = map(int, raw_input().split(' '))
print max(10*a + b+c, a+10*b + c, a+b + 10*c)