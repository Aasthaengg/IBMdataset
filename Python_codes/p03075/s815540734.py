l=[]
for i in range(5):l.append(int(input()))
k=int(input())
c=0
for i in l:
    for j in l:
        if abs(i-j)>k:c+=1
print('Yay!' if c==0 else ':(')