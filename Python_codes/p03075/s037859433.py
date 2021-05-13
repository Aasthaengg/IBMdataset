lst = []
for i in range(5):
    lst.append(int(input()))
k = int(input())    
lst.sort()
print(":(" if lst[-1] - lst[0] > k else "Yay!")