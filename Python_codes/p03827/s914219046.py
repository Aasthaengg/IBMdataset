N= map(int,input().split())
S = input()
syukei = [0,]
num = 0
count = 0
while len(S) > count:
    for i in S:
        count +=1
        if i == 'I':
            num +=1
            syukei.append(num)
        else:
            num -=1
            syukei.append(num)

print(max(syukei))