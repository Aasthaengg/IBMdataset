s=input()
k=int(input())

for i in s:
    if int(i)!=1:
        print(i)
        exit()
    k-=1
    if k<1:
        print(1)
        exit()

