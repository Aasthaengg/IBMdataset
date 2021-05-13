arr = []
temp = []
for i in range(3):
    t = list(map(int, input().split()))
    arr.append(t)
    temp.extend(t)
    
n = int(input())
for i in range(n):
    a = int(input())
    if a in temp:
        for i in range(3):
            for j in range(3):
                if arr[i][j] == a:
                    arr[i][j] = 'X'
                if arr[0][j] == arr[1][j] == arr[2][j] or  arr[0][0] == arr[1][1] == arr[2][2] or arr[0][2] == arr[1][1] == arr[2][0] or set(arr[i]) == {'X'}:
                    print('Yes')
                    exit()
        
print('No')