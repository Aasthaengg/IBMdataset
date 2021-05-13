n=int(input())
res = "No"
for sum in range(1,26):
    for j in range(sum+1):
        a=j
        b=sum-j
        if a*4 + b*7 ==n:
            res="Yes"
            break
print(res)
