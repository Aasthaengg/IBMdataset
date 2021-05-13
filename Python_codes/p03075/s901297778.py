a = []
for i in range(5):
    tmp = input()
    a.append(int(tmp))
k = int(input())
ans = True
for i in range(len(a)):
    for j in range(i, len(a)):
        if(a[j] - a[i] > k):
            ans = False
if ans:
    print("Yay!")
else:
    print(":(")