L, R = map(int, input().split())
target = R+1
if R - L > 2017:
    target = L + 2017
mi = 2019
for i in range(L,target):
    for j in range(i+1,target):
        mi = min(mi,(i*j)%2019)
print(mi)