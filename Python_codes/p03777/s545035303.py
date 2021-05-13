a,b = raw_input().split()
h = {'H':'D', 'D':'H'} if a == 'D' else {'H':'H', 'D':'D'}
print h[b]