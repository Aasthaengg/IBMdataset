R,G,B,N = map(int, input().split())
count=0

for i in range(N//R+1):
    for j in range(N//G+1):
        if (N-(R*i+G*j))<0:
            break
        if (N-(R*i+G*j))%B==0:
            count=count+1
print(count)