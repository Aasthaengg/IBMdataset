lst = [0 if x == 'H' else 1 for x in map(str,input().split())]
print('H' if sum(lst)%2 == 0 else 'D')