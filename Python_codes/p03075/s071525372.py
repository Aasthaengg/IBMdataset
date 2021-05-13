distances = []
for i in range(5):
    distances.append(int(input()))
k = int(input())

ans = 'Yay!'
for i in range(len(distances) - 1):
    for j in range(i + 1, len(distances)):
        if k < abs(distances[i] - distances[j]):
            ans = ':('
            
print(ans)