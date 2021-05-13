data = list(map(int, input().split()))
data.sort(reverse=True)
print(data[0]-data[1] + data[1]-data[2])
