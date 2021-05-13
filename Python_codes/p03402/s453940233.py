A,B = map(int,input().split())

ans = [["." for j in range(100)] for i in range(100)]

for i in range(50):#上半分は黒く塗りつぶす
    for j in range(100):
        ans[i][j]="#"


for i in range(A-1):
    ans[2*(i//50)][2*(i%50)]="."

for i in range(B-1):
    ans[51+2*(i//50)][2*(i%50)]="#"

print(100,100)
for i in range(100):
    print("".join(ans[i]))