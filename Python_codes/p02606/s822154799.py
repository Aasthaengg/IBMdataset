L, R, d = map(int, input().split())
myans = 0
for n in range(L,R+1):
    if n%d == 0:
        myans += 1
print(myans)