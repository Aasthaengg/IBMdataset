#C - Build Stairs
N = int(input())
H = list(map(int,input().split()))

target = H[0]
target_max = 0
result = 'Yes'
for i in range(1,N):
    if (H[i] < target - 1) or (target_max > H[i]):
        result = 'No'
        break
    elif H[i] == target - 1:
        target -= 1
    else:
        target = H[i] - 1
    target_max = max(target,target_max)           
print(result)