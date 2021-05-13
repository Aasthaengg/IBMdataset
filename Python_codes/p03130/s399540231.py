l1 = list(map(int,input().split()))
l2 = list(map(int,input().split()))
l3 = list(map(int,input().split()))

l = l1 + l2 + l3

cnt = []
for i in range(1,5):
    c = 0
    for j in l:
        if i == j:
            c += 1
    cnt.append(c)

cnt.sort()

if cnt == [1,1,2,2] :
    print("YES")
else:
    print("NO")   
