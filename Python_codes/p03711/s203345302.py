x,y = map(int,input().split())
A = [1,3,5,7,8,10,12]
B = [4,6,9,11]
C = [2]
ls = [A,B,C]
ans = 'No'
for i in range(3):
    if x in ls[i] and y in ls[i]:
        ans = 'Yes'
print(ans)