data = list(map(int, input().split()))
data.sort(reverse=True)
print( int(str(data[0]) + str(data[1])) + data[2] )
