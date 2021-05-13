X = int(input())

ans = 0
for i in range(1,40):
    for j in range(2,10):
        if X >= i**j and i**j > ans:
            ans = i**j

print(ans)