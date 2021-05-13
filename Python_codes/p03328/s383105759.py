
[a,b] = list(map(int,input().split()))

tou = []
dam=0
for i in range(1,1000):
    dam +=i
    tou.append(dam)
# print(tou)

X = b-a
print(tou[X-1] - b)