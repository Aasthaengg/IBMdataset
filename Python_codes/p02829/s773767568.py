a=int(input())
b=int(input())

tab=[1,2,3]

tab[a-1]=0
tab[b-1]=0

for j in range(3):
    if tab[j]!=0:
        print(tab[j])