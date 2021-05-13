n = []
ans = 'Yay!'
for i in range(6):
    n.append(int(input()))
for i in range(5):
    for j in range(5):
        if abs(n[i] - n[j]) > n[5]:
            ans = ':('
print(ans)
