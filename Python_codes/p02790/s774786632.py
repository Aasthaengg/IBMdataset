a,b = map(int,input().split())
A = str(a)*b
B = str(b)*a
ans=A if a<b else B
print(ans)