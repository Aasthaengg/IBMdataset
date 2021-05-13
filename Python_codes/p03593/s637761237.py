h,w=map(int,input().split())
s=[input() for _ in range(h)]
d=dict(zip([chr(i+97) for i in range(26)],[0]*26))
for i in range(h):
  for j in range(w):
    d[s[i][j]]+=1
a=[i%4 for i in d.values()]
print(['No','Yes'][a.count(1)+a.count(3)==h%2*w%2 and a.count(2)<=(h//2)*(w%2)+(w//2)*(h%2)])