arr=['Sunny','Cloudy','Rainy']
s=input()
ind=arr.index(s)
print (arr[(ind+1)%3])