N = int(input())
a = 'No'
for i in range(1, 9+1):
    for j in range(1, 9+1):
        ans = i * j
        if ans == N:
            a = 'Yes'
            break
print(a)
