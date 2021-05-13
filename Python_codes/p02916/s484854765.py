n = int(input())
a = list(map(int,(input().split()))) #食べた料理
b = list(map(int,(input().split()))) #料理iの満足度
c = list(map(int,(input().split()))) 

result = 0
mae = 1111
for i in a:
    #print("result",result)
    result += b[i-1]
    #print("mae,b[i-1]",mae,i)
    if mae == i -1:
        #print("if",result)
        result += c[i-2]
    mae = i

print(result)