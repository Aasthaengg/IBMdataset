import sys
input = sys.stdin.readline

n, m = [ int(v) for v in input().split() ]
num = [ int(v)-1 for v in input().split() ]
parent_list = [ i for i in range(n) ]

def root(x):
    while parent_list[x] != x:
        parent_list[x] = parent_list[parent_list[x]]  
        x = parent_list[x]   
    return x

for i in range(m):
    a, b = [ int(v)-1 for v in input().split() ]
    ra, rb = root(a), root(b)
    if ra != rb:
        parent_list[ra] = rb
        
ans_list = []
for i, v in enumerate(num):
    if root(i) == root(v):
        ans_list.append(True)
    else:
        ans_list.append(False)

print(ans_list.count(True))
