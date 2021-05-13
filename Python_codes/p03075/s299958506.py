l = []
cnt = 0
for i in range(5):
    l.append(int(input()))
    
k = int(input())

for i in range(len(l)):
    for j in range(len(l)):
        if i < j and abs(l[i] - l[j]) <= k:
            cnt += 1
            
if cnt == 10:
    print('Yay!')
else:
    print(':(')