k,x = map(int,input().split())
l = []

for i in range(x-k+1,k+x):
    l.append(str(i))

s = ''
for i in l:
    s += i
    s += ' '
print(s)