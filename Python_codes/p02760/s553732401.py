bingo = [list(map(int,input().split())) for i in range(3)]
n =  int(input())
num = [int(input()) for l in range(n)]
arr = [[],[],[]]

for number in num:
    cnt = 0
    for b in bingo:
        if number in b:
             arr[cnt].append(b.index(number))
        cnt  = cnt + 1

if len(arr[0]) == 3 or len(arr[1]) == 3 or len(arr[2]) == 3:
    print("Yes")
elif 0 in arr[0] and 1 in arr[1] and 2 in arr[2]:
    print("Yes")
elif 2 in arr[0] and 1 in arr[1] and 2 in arr[0]:
    print("Yes")
elif 0 in arr[0] and 0 in arr[1] and 0 in arr[2]:
    print("Yes")
elif 1 in arr[0] and 1 in arr[1] and 1 in arr[2]:
    print("Yes")
elif 2 in arr[0] and 2 in arr[1] and 2 in arr[2]:
    print("Yes")
else:
    print("No")