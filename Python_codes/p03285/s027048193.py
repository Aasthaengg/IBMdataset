n = int(input())
ans = 0
for i in range(30):
    for j in range(20):
        if 4*i + 7*j == n :
            ans +=1 
if ans:
    print("Yes")
else:
    print("No")