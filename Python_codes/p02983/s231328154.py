l,r=map(int,input().split())
d=range(l,r+1)[:673]
print(min(i*j%2019 for i in d for j in d if i<j))