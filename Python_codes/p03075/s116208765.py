abcde = [int(input()) for _ in range(5)]
k = int(input())
ans = 0
for i in range(4):
    for j in range(i+1,5):
        if abcde[j] - abcde[i] > k:
            ans += 1
if ans == 0:
    print('Yay!')
else:
    print(':(')
