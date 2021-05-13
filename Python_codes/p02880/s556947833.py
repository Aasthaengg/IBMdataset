N = int(input())
ans = 'No'

for i in range(1, 10):
    if ans == 'Yes':
        break

    for j in range(1, 10):
        if N == i * j:
            ans = "Yes"
            break
        else:
            ans = "No"
print(ans)
