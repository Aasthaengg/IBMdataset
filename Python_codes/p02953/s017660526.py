n = int(input())
al = list(map(int, input().split()))
cnt = len(al)
tmp = al[cnt-1]

for i in range(cnt-1, 1, -1):
    if al[i-1] - tmp >= 2:
        print("No") 
        exit()
    elif al[i-1] - tmp == 1:
        tmp = al[i-1]-1
    else:
        tmp = al[i-1]
print("Yes")