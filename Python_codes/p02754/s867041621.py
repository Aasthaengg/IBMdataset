score = list(map(int,input().split()))
gokei = score[1] + score[2]
shou,amari = score[0]//gokei,score[0] % gokei
if amari > score[1]:
    print((shou+1)*score[1])
else:
    print(shou*score[1]+amari)