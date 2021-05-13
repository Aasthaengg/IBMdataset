S = list(input())

count = 0
ans = 0
flg = False

for word in S:
    if word=="A" or word=="C" or word=="G" or word=="T":
        flg = True
    else:
        flg=False
        count = 0
    
    if flg:
        count += 1
    ans = max(ans,count)

print(ans)