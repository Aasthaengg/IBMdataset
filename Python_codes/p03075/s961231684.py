arr = [int(input()) for _ in range(5)]
k = int(input())
if max(arr)-min(arr)<=k:
    print('Yay!')
else:
    print(':(')
