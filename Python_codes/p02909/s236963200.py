S = input()
wdict = ["Sunny","Cloudy","Rainy"]

now = wdict.index(S)
nextw = (now+1) % 3
print(wdict[nextw])