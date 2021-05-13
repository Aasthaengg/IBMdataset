n = int(input())

v = list(map(int,input().split()))
c = list(map(int,input().split()))
l =[]
l_max = 0

for i in range(n):
    l.append(v[i]-c[i])
#print(sorted(l,reverse = True))

for i in l:
    if l_max < l_max+i:
        l_max += i

print(l_max)