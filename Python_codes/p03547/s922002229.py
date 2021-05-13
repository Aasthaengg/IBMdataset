x,y = map(str,input().split())
print(">") if ord(x)>ord(y) else print("<") if ord(x)<ord(y) else print("=")