X = int(input())
ans = 0
for i in range(1,X+1):
    for j in range(2,11):
        tmp = i**j
        if ans < tmp <= X:
            ans = tmp
print(ans)