A,B,C = map(int,input().split())
array = [A,B,C]
array.sort()
print(int(array[0]*array[1]/2))