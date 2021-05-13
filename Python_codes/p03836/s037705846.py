sx, sy, tx, ty=map(int,input().split())

hrz=tx-sx
vrt=ty-sy

a="U"*vrt
b="R"*hrz
c="D"*vrt
d="L"*hrz
ans1=a+b+c+d
a2=a+"U"
b2=b+"R"
c2=c+"D"
d2=d+"L"
ans2="L"+a2+b2+"DR"+c2+d2+"U"
print(ans1+ans2)