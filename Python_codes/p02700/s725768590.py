a,b,c,d = map(int,input().split())
print("Yes" if (a+d-1)//d >= (b+c-1)//b else "No")