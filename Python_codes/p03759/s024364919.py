a,b,c = map(int,input().split())
ba = b-a
cb = c-b
if ba == cb:
    print("YES")
else:
    print("NO")
