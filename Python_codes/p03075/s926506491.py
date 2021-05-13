l=[]
for _ in range(5):
    l.append(int(input()))
k = int(input())
print('Yay!' if l[-1] - l[0]<=k else ':(')