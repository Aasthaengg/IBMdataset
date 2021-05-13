li = list(map(int,input().split()))
xy1,xy2 = (li[0],li[1]),(li[2],li[3])
div=(xy2[0]-xy1[0],xy2[1]-xy1[1])
print(xy2[0]-div[1],xy2[1]+div[0],xy1[0]-div[1],xy1[1]+div[0],sep=" ")