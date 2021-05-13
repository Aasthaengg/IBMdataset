n,k,c = map(int,input().split())
s = input()
l = [0]*k
r = [0]*k

count = 0
bef = 0
for i,j in enumerate(s):
    if j == 'o':
        if count == 0:
            l[0] = i+1
            count += 1
            bef = i
        elif i > bef + c:
            l[count] = i+1
            count += 1
            bef = i
    if count == k:
        break

count = 0
bef = 0
for i,j in enumerate(s[::-1]):
    if j == 'o':
        if count == 0:
            r[0] = n-i
            count += 1
            bef = i
        elif i > bef + c:
            r[count] = n-i
            count += 1
            bef = i
    if count == k:
        break
r = r[::-1]

for i in range(k):
    if l[i] != 0 and l[i] == r[i]:
        print(l[i])