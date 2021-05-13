list = list(map(int,input().split()))
ans = (60-list[1])+list[3]+(list[2]-list[0]-1)*60-list[4]
print(ans)