import math
t = 1
for tc in range(t):
    n = int(input())
    arr =  []
    for i in range(n):
        lst = list(map(int, input().split()))
        # print(n1,n2)
        arr.append(lst)
        # print(arr)
    # print(arr)
    ans = False
    for i in range(n-2):
        if arr[i][0] == arr[i][1] and arr[i+1][0] == arr[i+1][1] and arr[i+2][0] == arr[i+2][1] :
            ans = True
            break
    if ans == True:
        print("Yes")
    else:
        print("No")
        

    
    
