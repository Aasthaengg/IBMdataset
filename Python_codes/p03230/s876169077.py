n = int(input())

cnt = 0
fitn = 0
while(fitn < n):
    cnt += 1
    fitn += cnt
    
    if(fitn > n):
        print("No")
        exit()


numofrow = cnt + 1
ans = []
for i in range(numofrow):
    ans.append([])
offset = 0
finishrow = 0
while(finishrow != numofrow):
    for i in range(cnt-finishrow):
        ans[finishrow].append(i+1+offset)
    finishrow += 1    
    for i in range (numofrow-finishrow):
        ans[i+finishrow].append(i+1+offset)
    
    offset += numofrow-finishrow

print("Yes")
print(numofrow)
for i in range(numofrow):
    print(cnt," ".join(map(str,ans[i])))