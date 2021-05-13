"""
A
>
B
 のときGREATER、
A
<
B
 のときLESS、
A
=
B
 のときEQUALと出力せよ。

"""
A,B=map(int,open(0).read().split())
if A>B:ans="GREATER"
if A<B:ans="LESS"
if A==B:ans="EQUAL"
print(ans)