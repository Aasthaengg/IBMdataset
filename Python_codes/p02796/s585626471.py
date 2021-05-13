M,*li = [list(map(int,i.split())) for i in open(0)]
M = M[0]
row = [[x-y,x+y] for x,y in li]
row.sort(key = lambda x:x[1])
ans = 0
s = -1*float('inf')
for rs,rt in row:
    if s <= rs:
        ans += 1
        s = rt
print(ans)