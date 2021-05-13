n = int(input())
v = list(map(int,input().split()))
for i in range(n-1):v.sort();v.append((v[0]+v[1])/2);del v[:2]
print(v[0])