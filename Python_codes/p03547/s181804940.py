a,b=map(str,input().split())
l=["A","B","C","D","E","F"]
if l.index(a)<l.index(b):
    print("<")
elif l.index(a)==l.index(b):
    print("=")
else:
    print(">")