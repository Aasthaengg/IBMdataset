N= int(input())
A  = list(map(int,input().split()))
B  = list(map(int,input().split()))
short = []
margine = []
for a,b in zip(A,B):
    if a > b :
        margine.append(a-b)
    elif b > a:
        short.append(b-a)
        
ss = sum(short)
sc = len(short)
margine = sorted(margine)
if ss>sum(margine):
    print(-1)
    exit()
while ss>0:
    ss -= margine.pop()
    sc += 1
print(sc)

