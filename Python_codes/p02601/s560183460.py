a,b,c = map(int,input().split())
k = int(input())
cnt = 0
cnt2 = 0
ans = "No"
for i in range(k):
    if a < b:
        break
    else:
        b = b * 2
        cnt +=1
for i in range(k-cnt):
    if b < c:
        break
    else:
        c = c * 2
        cnt2 +=1
        
if a < b and b < c and cnt + cnt2 <=k:
    print("Yes")
else:
    print("No")