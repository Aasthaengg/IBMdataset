l = [int(input()) for i in range(5)]
k = int(input())

for i in range(5):
    for j in range(i+1,5):
        if abs(l[i] - l[j]) > k:
            print(':(')
            exit()
print('Yay!')