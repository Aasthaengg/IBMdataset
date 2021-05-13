h = list(map(int, input().split()))

if h[1] < h[3]:
    print((h[2]-h[0])*60+h[3]-h[1]-h[4])
else:
    print((h[2]-h[0]-1)*60+60-h[1]+h[3]-h[4])
    
