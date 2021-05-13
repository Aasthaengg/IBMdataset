n = int(input())
l = map(int,input().split())

l = sorted(l,reverse=True)

l2 = []

for i in range(1,2*n+1,2):
    l2.append(l[i])
    

print(sum(l2))