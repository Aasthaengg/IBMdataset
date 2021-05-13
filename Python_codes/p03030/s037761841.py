n = int(input())
l = [input().split() for i in range(1,n+1)]

for i in range(1,n+1):
    l[i-1].append(i)
#print(l)

for i in range(n):
    l[i][1] = (int(l[i][1]))*(-1)
#print(sorted(l))
sl = sorted(l)

#ans = sorted(l.sort(),reverse = True, key = lambda x:x[1])
#print(ans)

for i in range(n):
    print(sl[i][2])