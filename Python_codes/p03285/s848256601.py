n = int(input())
ans = "No"
for i in range((n//4)+1):
    for j in range((n//7)+1):
        if (i*4)+(j*7)==n:
            ans = "Yes"
            break
print(ans)
