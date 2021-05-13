a,b,c = map(int,input().split())
k = int(input())
for i in range(k):
    if b >= c:
        c = c*2
    elif b <c and a>=b:
        b = b*2
if a<b and b<c:
    print("Yes") 
else:
    print("No")        