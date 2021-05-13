n = int(input())
lst =  []
stimmt = False
for _ in range(n):
    lst.append(list(map(str,input().split())))
for i in range(len(lst)):
    if lst[i][0] == lst[i][1]:
        if i+2 < len(lst):
            if lst[i+1][0] == lst[i+1][1] and lst[i+2][0] == lst[i+2][1]:
                stimmt = True
                break
 
if stimmt:
    print("Yes")
else:
    print("No")