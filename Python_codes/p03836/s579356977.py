sx,sy,tx,ty = map(int,input().split())
ans = []
ans_out2 = ["D"]
ans_re2 = ["U"]

def solve(sx,sy,tx,ty):
    for i in range(tx-sx):
        ans.append("R")
    for i in range(ty-sy):
        ans.append("U")
    for i in range(tx-sx):
        ans.append("L")
    for i in range(ty-sy):
        ans.append("D")

    for i in range(tx-sx+1):
        ans_out2.append("R")
    for i in range(ty-sy+1):
        ans_out2.append("U")
    ans_out2.append("L")

    for i in range(tx-sx+1):
        ans_re2.append("L")
    for i in range(ty-sy+1):
        ans_re2.append("D")
    ans_re2.append("R")

    list = ans+ans_out2+ans_re2

    return list
  
ans_list = solve(sx,sy,tx,ty)
    
for i in range(len(ans_list)):
    print(ans_list[i],end="")