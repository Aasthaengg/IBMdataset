l,r=map(int,input().split())
d=range(l,r+1)
print(0 if r-l>671 else min(i*j%2019 for i in d for j in d if i<j))