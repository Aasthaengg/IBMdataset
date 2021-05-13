N = int(input())

lucas = [2,1]
for i in range(2,N+1):
    lucas_num = lucas[i-1] + lucas [i-2]
    lucas.append(lucas_num)
print(lucas[-1])