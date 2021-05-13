sx, sy, tx, ty = map(int, input().split())
ver = ty - sy
hor = tx - sx
go1 = 'U'*ver+"R"*hor
back1 = "D"*ver+"L"*hor
go2 = "D"+"R"*(hor+1)+'U'*(ver+1)+"L"
back2 = "U"+"L"*(hor+1)+"D"*(ver+1)+"R"
print(go1+back1+go2+back2)