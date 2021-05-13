n=int(input())
a=input()
L=[]
for i in range(26):
    L.append(chr(65+i))
news=''
for i in range(len(a)):
  news+=L[L.index(a[i])+n-26]
print(news)
  
