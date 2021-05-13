lis = []

for _ in range(5):
    lis.append(int(input()))
    
k = int(input())

for i in range(5):
    for j in range(i+1, 5):
        if (lis[j] - lis[i]) > k:
            print(":(")
            exit()

print("Yay!")