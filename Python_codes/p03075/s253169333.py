a =[]
for i in range(5):
    a.append(int(input()))
k = int(input())
x = max(a)
y = min(a)
if x-y > k:
    print(':(')
else:
    print('Yay!')