X = int(input())

ans = 0

for i in range(1, 32):
    for j in range(2, 11):
        exp = i**j
        if exp <= X:
            ans = max(ans, exp)
        else:
            break
            
print(ans)