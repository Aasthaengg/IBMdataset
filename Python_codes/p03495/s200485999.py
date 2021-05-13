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

INF = 10**8
data1 = datain(2)
data2 = datain(data1[0])
count = [INF for i in range(data1[0]+1)]
num = 0
ans = 0

for val in data2:
    if count[val] == INF:
        count[val] = 0
        num += 1
    count[val] += 1

count.sort()
#print(count);print(num)

if num >= data1[1]:
    for val in count[0:(num-data1[1])]:
        ans += val

print(ans)