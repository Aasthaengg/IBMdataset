data = list(map(int,input().split()))

if data[1]%data[0] == 0:
    print(sum(data))
else:
    print(data[1]-data[0])
