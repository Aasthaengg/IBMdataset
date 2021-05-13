import collections
h,w=map(int,input().split())
a=""
for i in range(h):
    a+=input()
f,o=1,0
for i in collections.Counter(a).values():
    f+=i//4
    o+=i&1
print(["No","Yes"][f>(h//2)*(w//2) and o<=h%2*w%2])