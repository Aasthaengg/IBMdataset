num = int(input())
input_line = list(map(int,input().split(' ')))
flower = [0 for i in range(num)]
cnt = 0
while(True):
    flg = 0
    for n in range(num):
        if(flower[n] != input_line[n]):
            flower[n] += 1
            flg = 1
        elif(flg):
            flg = 0
            cnt += 1
        if(flg and (n==(num-1))):
            cnt += 1
    if(sum(flower) == sum(input_line)):
        break
print(cnt)
