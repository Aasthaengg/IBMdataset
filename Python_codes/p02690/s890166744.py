x = int(input())
flg = 0
for i in range(-118,120,1):
    for j in range(-119,119,1):
        if (i)**5 - (j)**5 == x:
            ans1 = i
            ans2 = j
        
print(str(ans1)+str(" ")+str(ans2))