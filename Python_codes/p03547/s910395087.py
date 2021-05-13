x,y=map(lambda x: x,input().split())
x,y=ord(x),ord(y)
print("<" if x<y else ">" if x>y else "=" )