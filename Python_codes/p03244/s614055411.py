n = int(input())
v = [i for i in input().split()]
v1 = {}
v2 = {}
for i in range(n//2):
    if  v[2 *i +1] in v1.keys():
        v1[v[2 * i +1]] += 1
    else:
        v1[v[2 * i + 1]] = 1

    if v[2 * i] in v2.keys():
        v2[v[2 * i]] += 1
    else:
        v2[v[2 * i]] = 1
v1 = sorted(v1.items(),key=lambda x:  x[1])
v2 = sorted(v2.items(),key=lambda x:  x[1])
v1.reverse()
v2.reverse()
v1.append((None,0))
v2.append((None,0))
#print(v1)
if v1[0][0] == v2[0][0]:
    ans = max(v1[0][1]+v2[1][1] , v1[1][1] + v2[0][1])
else:
    ans = v1[0][1] + v2[0][1]
print(n - ans)