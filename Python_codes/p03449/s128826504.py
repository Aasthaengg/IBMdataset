N = int(input())
array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
array = [array1,array2]
candy = [0]*N
for i in range(N):
    candy[i] = sum(array[0][0:i+1])+array[1][i]+sum(array[1][i+1:N])
print(max(candy))