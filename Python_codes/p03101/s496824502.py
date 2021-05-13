data = list(map(int,input().split()))
data2 = list(map(int, input().split()))

print(data[0]*data[1]-data2[0]*data[1]-(data[0]-data2[0])*data2[1])
