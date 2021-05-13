n = int(input())

l = []
for i in range(n):
    x,y = input().split()
    y = int(y)
    l.append([x,y,i])
l.sort(key=lambda x:x[1],reverse=True)
l.sort(key=lambda x:x[0])

for s in l:
    print(s[2]+1)