times = int(input())
element = []

for i in range(times):
    element.append(int(input()))

maxv = element[1]-element[0]
minv = element[0]
for j in range(1,len(element)):
    maxv = max(element[j]-minv,maxv)
    minv = min(minv,element[j])

print(maxv)