arr = []
arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))
arr.append(list(map(int, input().split())))

def checker(arr):
    if arr[0][0] == arr[0][1] == arr[0][2] == "X":
        return True
    if arr[1][0] == arr[1][1] == arr[1][2] == "X":
        return True
    if arr[2][0] == arr[2][1] == arr[2][2] == "X":
        return True
    if arr[0][0] == arr[1][0] == arr[2][0] == "X":
        return True
    if arr[0][1] == arr[1][1] == arr[2][1] == "X":
        return True
    if arr[0][2] == arr[1][2] == arr[2][2] == "X":
        return True
    if arr[0][0] == arr[1][1] == arr[2][2] == "X":
        return True
    if arr[0][2] == arr[1][1] == arr[2][0] == "X":
        return True
    return False

for i in range(int(input())):
    a = int(input())
    for i in range(3):
        for j in range(3):
            if arr[i][j] == a:
                arr[i][j] = "X"
    
if checker(arr): print("Yes")
else: print("No")