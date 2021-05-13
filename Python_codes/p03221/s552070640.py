# 初期入力
import sys
input = sys.stdin.readline  #文字列では使わない
Ken_n,City_n = (int(i) for i in input().split())
city ={i:[] for i in range(1,Ken_n+1)}
for i in range(1,City_n+1):
    p,y = (int(i) for i in input().split())
    city[p].append((y,i))

city_ID ={i:0 for i in range(1,City_n +1)}
for i in range(1,Ken_n +1):
    city[i].sort()
    
    for j in range(len(city[i])):
        city_ID[city[i][j][1]] = "{0:06d}".format(i) +"{0:06d}".format(j+1)

for i in range(1,City_n +1):
    print(city_ID[i])