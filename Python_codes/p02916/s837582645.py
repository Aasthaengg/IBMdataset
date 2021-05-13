n = int(input())
a = [ i for i in list(map(int,input().split()))]
b = [j for j in list(map(int,input().split()))]
c = [k for k in list(map(int,input().split()))]
c.append(0)
count  = 0
prev = 0
for o in a:
    count += b[o-1]
    if o == prev +1:
        count +=c[o-2]
        prev = o
    else:
        prev = o
print(count)