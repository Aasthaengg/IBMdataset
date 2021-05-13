A,B,C,D=map(int,input().split())
L=A+B
R=C+D
if L>R:
    ans="Left"
elif L<R:
    ans="Right"
else:
    ans="Balanced"
print(ans)