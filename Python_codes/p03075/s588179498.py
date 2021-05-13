d = [int(input()) for i in range(5)]
k = int(input())
ans = 'Yay!'
for i in d:
    for j in d:
        if abs(i-j)>k:
            ans = ':('
print(ans)
