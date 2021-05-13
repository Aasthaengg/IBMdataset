L = []
for i in range(5):
    L.append(int(input()))
k = int(input())
if L[4]-L[0] > k:
    print(":(")
else:
    print("Yay!")