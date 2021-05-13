
h1,m1,h2,m2,k=map(int,input().split())
all=0
if m2>=m1:
    all += (h2-h1)*60 + (m2-m1)
    all -= k
else:
    all += (h2-1-h1)*60 + (m2+60-m1)
    all -= k
print(all)