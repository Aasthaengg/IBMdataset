N = int(input().strip())
array=[]
for i in range(N):
    x=int(input().strip())
    array.append(x)
set(array)
l=list(set(array))
print(len(l))