L ,R = map(int,input().split())

ans =[]
for i in range(L,R+1):
    for j in range(i+1,R+1):
        ans.append(i*j%2019)
        if (i * j % 2019) == 0:
            break
    else:
        continue
    break

print(min(ans))