N = int(input())
d = list(map(int,input().split()))

count = 0
count2 = 0
d.sort()

le = len(d)//2
s = d[int(le)-1]
l = d[int(le)]
ans = 0
for i in range(s,l):
  ans += 1
if(ans == ""):
	print(0)
else:
    print(ans)