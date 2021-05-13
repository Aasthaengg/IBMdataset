A,B,C = map(int,input().split())
K = int(input())
array = []
for i in range(3):
    array.append([A,B,C])

for i in range(3):
    array[i][i] *= 2**K

print(max(sum(array[0]),sum(array[1]),sum(array[2])))
    

