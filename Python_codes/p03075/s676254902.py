arr = []
for i in range(5):
    arr.append(int(input()))
k = int(input())
if max(arr) - min(arr) > k:
    print(':(')
else:
    print('Yay!')