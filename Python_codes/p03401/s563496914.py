n=int(input())
lst=list(map(int,input().split()))
idou=[abs(lst[0])]
for i in range(1,n):
    idou.append(abs(lst[i]-lst[i-1]))
idou.append(abs(lst[-1]))
kyori=sum(idou)


kyo=kyori-(idou[0]+idou[1])
kyo+=abs(lst[1])
print(kyo)

for i in range(1,n-1):
    kyo=kyori-(idou[i]+idou[i+1])
    kyo+=(abs(lst[i+1]-lst[i-1]))
    print(kyo)

kyo=kyori-(idou[-1]+idou[-2])
kyo+=abs(lst[-2])
print(kyo)