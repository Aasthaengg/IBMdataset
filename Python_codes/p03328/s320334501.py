
a,b = map(int,input().split())
diff = abs(b-a)
r = 0

for i in range(1,diff+1):
    r += i
print(r-b)
