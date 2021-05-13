sx, sy, tx, ty = map(int, input().split())

ans = []
ans += (ty-sy) * "U" + (tx-sx) * "R" + (ty-sy) * "D" + (tx-sx) * "L"

ans += "L" + (ty-sy+1) * "U" + (tx-sx+1) * "R" + "D"
ans += "R" + (ty-sy+1) * "D" + (tx-sx+1) * "L" + "U"

print("".join(ans))