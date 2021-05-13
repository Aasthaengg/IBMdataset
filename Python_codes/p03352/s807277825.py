X = int(input())
final = 0
for i in range(40):
    for j in range(2,11):
        if i**j > X:
            final = max(ans,final)
            break
        ans = i**j
print(final)