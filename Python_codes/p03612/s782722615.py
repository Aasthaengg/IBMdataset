n = int(input())

p = [int(i) for i in input().split()]

cout = 0
temp_cout = 0

for i in range(len(p)):
    num = i+1
    if num == p[i]:
        cout +=1
        temp_cout +=1
    else:
        temp_cout = 0
        
    if temp_cout == 2:
        temp_cout = 0
        cout -= 1
        
print(cout)