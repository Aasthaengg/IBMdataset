a = [int(input()) for _ in range(5)]
k = int(input())

flag = True

for i in range(4):
    for j in range(i+1, 5):
        if abs(a[i] - a[j]) > k:
            flag = False
            break

if flag:
    print("Yay!")
else:
    print(":(")