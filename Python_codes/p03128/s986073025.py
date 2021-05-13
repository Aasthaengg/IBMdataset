n , m = map(int, input().split(' '))
s = [0,2,5,5,4,5,6,3,7,6]
a = list(map(int, input().split(' ')))
r = []
for i in range(len(a)):
    r.append([s[a[i]],a[i]])
r.sort()
d = [-1]*(n+1)
d[0] = 0
for i in range(1,n+1):
    j = 0
    while j < len(a):
        if i-s[r[j][1]] < 0:
            j += 1
        elif d[i-s[r[j][1]]] >= 0:
            d[i] = d[i-s[r[j][1]]] +1
            break
        else:
            j+= 1
result = []
a.sort(reverse = True)
while n > 0:
    j = 0
    while j < len(a):
        if n < s[a[j]]:
            j += 1
        elif d[n-s[a[j]]] +1 == d[n]:
            result.append(a[j])
            n -= s[a[j]]
            break
        else:
            j += 1
print(''.join(list(map(str, result))))