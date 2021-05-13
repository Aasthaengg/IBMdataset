a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
ans = 0
for i in range(4):
    for j in range(i+1, 5):
        if a[j] - a[i] > k:
            ans = 1
if ans == 1:
    print(':(')
else:
    print('Yay!')