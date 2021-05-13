X = int(input())

ans=[]
for i in range(-501,501):
    for j in range(-500,501):
        sum = i**5 - j**5
        if sum == X:
            ans.append(i)
            ans.append(j)
            print(*ans)
            exit()