n,k = map(int,input().split())
num_list = list(map(int,input().split()))
ans = 10e12
for i in range(n-k+1):
    left = num_list[i]
    right = num_list[i+k-1]
    if (right <= 0) and (left <= 0):
        tmp = abs(left)
    elif (right >= 0) and (left <= 0):
        tmp = min(abs(right) , abs(left)) + abs(right) + abs(left)
    elif (right >= 0) and (left >= 0):
        tmp = abs(right)
    if tmp < ans:
        ans = tmp
print(ans)