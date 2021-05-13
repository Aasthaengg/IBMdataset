n = int(input())
abl = [list(map(int,input().split())) 
       for nesya in range(n)]
abl.sort()
print(abl[-1][1]+abl[-1][0])