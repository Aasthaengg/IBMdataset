n = int(input())

ans = []
for i in range(1, n + 1):
    x = i
    for j in range(100):
        if x % 2 == 0:
            x = int(x // 2)
            #ans.append(j)
        else:
            #ans.append(j)
            break
    ans.append(j)

#print(ans)
print(ans.index(max(ans)) + 1)
