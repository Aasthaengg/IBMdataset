a = list(map(int,[input() for i in range(5)]))
k = int(input())

ans = True
for i in range(5):
    for j in range(i+1,5):
        if (a[j]-a[i]) > k:
            ans = False

if ans:
    print('Yay!')
else:
    print(':(')