l,r = map(int,input().split())
p = 2019
if r - l >= 2019:
    for i in range(l,l+2019):
        for j in range(i+1,l+2020):
            p = min(p,i*j%2019)
            if p == 0:
                print(0)
                exit(0)
else:
    for i in range(l,r):
        for j in range(i+1,r+1):
            p = min(p,i*j%2019)
            if p == 0:
                print(0)
                exit(0)
print(p)