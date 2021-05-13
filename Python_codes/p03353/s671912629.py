# solution

data = input()

qwe = int(input())

dic = set()

for i in range(len(data)):
    for j in range(qwe):
        if i+j+1 <= len(data):
            dic.add(data[i:i+j+1])
di = list(dic)
di.sort()
print(di[qwe-1])