count = [0]*5
for i in range(3):
    a,b = [int(j) for j in input().split()]
    count[a]+=1
    count[b]+=1
for i in range(1,5):
    if count[i] == 3:
        print("NO")
        exit()
print("YES")