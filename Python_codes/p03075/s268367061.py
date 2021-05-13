a=[]
for i in range(5):
    a.append(int(input()))
k = int(input())
ans = 0
for i in range(len(a)):
    for j in range(i,len(a)):
        if abs(a[j]-a[i]) > k:
            ans += 1
print('Yay!' if ans == 0 else ':(')
