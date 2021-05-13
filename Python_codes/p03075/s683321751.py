a = []
for i in range(5):
    a.append(int(input()))
k = int(input())
is_true = True
for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[j] - a[i] > k:
            is_true = False
            break
if is_true:
    print("Yay!")
else:
    print(":(")