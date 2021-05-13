s=input()
l=["Sunny","Cloudy","Rainy"]
index=l.index(s)
index+=1
if index==3:
    index=0
print(l[index])