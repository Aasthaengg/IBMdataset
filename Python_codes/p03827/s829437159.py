N=int(input())
S = input()
x = 0
max_x = 0
for i in S:
    if i =="I":
        x +=1
    else:
        x -=1
    max_x = max(x,max_x)
print(max_x)