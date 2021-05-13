a,b = map(int, raw_input().split(' '))
l=['a < b','a > b','a == b']
for s in l:
    if eval(s):
        print s