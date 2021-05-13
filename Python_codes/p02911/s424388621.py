N,K,Q = map(int,input().split())

li = [0]*N

for _ in range(Q):
    index = int(input())-1
    li[index]+=1


for num in li:
    if K>Q-num:
        print("Yes")
    else:
        print("No")