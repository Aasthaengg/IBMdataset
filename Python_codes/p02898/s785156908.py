n,k=map(int, input().split())
h_list=[int(i) for i in input().split()]
count=0

for i in h_list:
    if i>=k:
        count+=1
        
print(count)