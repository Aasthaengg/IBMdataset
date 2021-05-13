st = list(map(int,input().split()))
x = st[2] - st[0]
y = st[3] - st[1]
l1 = 'U'*y + 'R'*x
l2 = 'D'*y + 'L'*x
l3 = 'L' + 'U'*(y+1) + 'R'*(x+1) + 'D'
l4 = 'R' + 'D'*(y+1) + 'L'*(x+1) + 'U'
print(l1+l2+l3+l4)