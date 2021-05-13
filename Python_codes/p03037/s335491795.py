n,m = map(int,input().split(' '))
l = []
start = 0
end = n+1
count = 0

for i in range(m):
    l.append(list(map(int,input().split(' '))))

for i in l:
    if i[0] >= start:
        start = i[0]
    if i[1] <= end:
        end = i[1]
if start > end:
    print(0)
else:
    print(end-start+1)