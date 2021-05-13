dic={"x":"y","y":"x"}

a = list(input())
X,Y = map(int,input().split())

direction = "x"
cersol = 0
while cersol < len(a) and a[cersol] == "F":
    cersol+=1
    X -= 1#これは確定した動きなので目的地をずらす方が楽

move = {"x":[],"y":[]}

while cersol < len(a):
    if a[cersol]=="T":#ターンならターン
        direction=dic[direction]
        cersol+=1

    count = 0
    while cersol < len(a) and a[cersol] == "F":
        count+=1
        cersol+=1
    
    move[direction].append(count)


able = {0:0}
preable = {0:0}
for i in move["x"]:
    able={}
    for j in preable:
        able[j+i]=0
        able[j-i]=0
    preable=able


ableX = able

able = {0:0}
preable = {0:0}
for i in move["y"]:
    able = {}
    for j in preable:
        able[j+i]=0
        able[j-i]=0
    preable=able

if (X in ableX)and(Y in able):
    print("Yes")
else:
    print("No")
