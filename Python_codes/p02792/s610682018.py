n = int(input())
arr = [[0]*10 for i in range(10)]
for i in range(1, n+1):
    i = str(i)
    arr[int(i[0])][int(i[-1])]+=1
s = 0
t = 0
# print(arr)
for i in range(10):
    for j in range(10): t+=arr[i][j]*arr[j][i]
    s+=t
print(t)
    
