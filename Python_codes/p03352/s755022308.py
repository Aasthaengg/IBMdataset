a=int(input())
result=[]
for i in range(1,a+1):
    for j in range(2,a+1):
        if j>=10:
            continue
        if i**j<=a:
            result.append(i**j)
result.append(1)
print(max(result))