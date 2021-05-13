lis = ['Sunny', 'Cloudy', 'Rainy']
S = input()
idx = lis.index(S)
if idx==2:
    print(lis[0])
else:
    print(lis[idx+1])