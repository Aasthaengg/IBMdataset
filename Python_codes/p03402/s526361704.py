A,B = map(int,input().split())
print("100 100")
ans = [["#"]*100 for _ in range(50)] + [["."]*100 for _ in range(50)]
A -=1
B -=1

wR = 0 
while A>=50:
    A -= 50
    for i in range(0,100,2):
        ans[wR][i]="."
    wR += 2
     
wC = 0
while A>0:
    A -= 1
    ans[wR][wC]="."
    wC += 2
    
bR=99
while B>=50:
    B -= 50
    for i in range(0,100,2):
        ans[bR][i]="#"
    bR -= 2
    
bC = 0
while B>0:
    B -= 1
    ans[bR][bC]="#"
    bC += 2

[print("".join(i)) for i in ans]
