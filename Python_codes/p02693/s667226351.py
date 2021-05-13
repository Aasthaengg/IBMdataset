k = int(input())
a,b = map(int,input().split())
chk = False

for i in range(a,b+1):
    if i % k == 0:
        chk = True
        break
      
print("OK") if chk else print("NG")