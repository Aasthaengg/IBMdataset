def f(s,t): return t[:-1] == s and len(t) == len(s) + 1
s = raw_input()
t = raw_input()#.split()
print 'Yes' if f(s,t) else 'No'
