N = int(input())
arr = [[[0 for i in range(10)] for j in range(3)]for r in range(4)]
for i in range(N):
    a=[]
    a.append(list(map(int,input().split())))
    b=a[0][0]-1
    f=a[0][1]-1
    r=a[0][2]-1
    v=a[0][3]
    arr[b][f][r]+=v

for i in range(0,3):
    for j in range(0,3):
        print(" "+" ".join(map(str,arr[i][j])))
    print("#"*20)
for i in range(3):
    print(" "+" ".join(map(str,arr[3][i])))