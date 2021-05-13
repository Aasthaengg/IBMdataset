n = int(input())
lis = list(map(int, input().split()))

lis  =sorted(lis)

t1 = sum(lis[n:2*n])
#print(sum(t1))

nlis = lis[::-1]

t2 = 0
for i in nlis[1:2*n:2]:
    t2 += i


print(max(t1, t2))