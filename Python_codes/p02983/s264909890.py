L, R = map(int, input().split())
ama=[]
for i in  range(L,R+1):
    amari = i%2019
    if amari ==0:
        print(amari)
        exit()
minimi = 2019
for j in range(L,R+1):
    for s in range(j+1,R+1):
        waka = (j*s)%2019
        minimi = min(minimi,waka)
print(minimi)