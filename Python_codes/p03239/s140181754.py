n,t = map(int,input().split())
li = []
for i in range(n):
    a,b = map(int,input().split())
    if b <= t:
        li.append(a)
if len(li) >= 1:
    print(min(li))
else:
    print("TLE")