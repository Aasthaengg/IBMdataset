#複数の整数入力を受け付ける関数
def datain(num):

    data = []
    iscnt = True

    while iscnt:
        for val in map(int,input().split()):
            data.append(val)
            if len(data) == num:
                iscnt = False
                break
        
    return data

num = int(input())
data = datain(num*3)
data.sort()
ans = 0

for i in range(num*3-2,num-1,-2):
    #print(i)
    ans += data[i]

#print(data)
print(ans)