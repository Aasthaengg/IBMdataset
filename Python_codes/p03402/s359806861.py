a,b=map(int, input().split())
k=50
MAP=[]
for _ in range(k):
    MAP.append(["#"]*2*k)
for _ in range(k):
    MAP.append(["."]*2*k)
a-=1
b-=1
for i in range(0,k-1,2):
    for j in range(0,2*k,2):
        if a>0:
            MAP[i][j]="."
            a-=1
for i in range(k+1,2*k,2):
    for j in range(0,2*k,2):
        if b>0:
            MAP[i][j]="#"
            b-=1
print(2*k,2*k)
for i in MAP:
    print("".join(i))