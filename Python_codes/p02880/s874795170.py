N = int(input())
ans = "No"
for i in range(1,10):
    div,mod = divmod(N,i)
    if (mod == 0) and (div < 10):
        ans = "Yes"
        break
        
print(ans)