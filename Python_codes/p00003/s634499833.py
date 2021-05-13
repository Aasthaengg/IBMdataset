n = int(input())
array = [[int(i) for i in input().split()] for i in range(n)]
for i in range(n):
    if array[i][0]**2+array[i][1]**2 == array[i][2]**2:
        print("YES")
    elif array[i][0]**2+array[i][2]**2 == array[i][1]**2:
        print("YES")
    elif array[i][1]**2+array[i][2]**2 == array[i][0]**2:
        print("YES")
    else:
        print("NO")