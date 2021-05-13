( r, c) = [int(i) for i in  input().split()]
num = []
for i in range(r):
    num.append( [ int(i) for i in input().split()])
    #sum r
    num[i].append( sum( num[i]))

# sum c
last_row = [ 0 for _ in range( c+1)]
for rc in range(r):
    for cc in range( c+1):
        last_row[cc] += num[rc][cc]
num.append( last_row)
'''
for i in range(r):
     print( sum( [ num[js] for js in range(c)])
    #last_row[i] = sum( [ num[js] for js in range(c)])
'''

for rc in range( r+1):
    print( ' '.join( [ str(a) for a in num[rc]]))