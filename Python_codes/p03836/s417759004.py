sx, sy, tx, ty = map(int, input().split())
 
dx = abs(tx - sx)
dy = abs(ty - sy)

s = ["L"]+["U"]*(dy+1)+["R"]*(dx+1)+["D"] + ["R"]+["D"]*(dy+1)+["L"]*(dx+1)+["U"] + ["U"]*dy+["R"]*dx + ["D"]*dy+["L"]*dx
print("".join(s))