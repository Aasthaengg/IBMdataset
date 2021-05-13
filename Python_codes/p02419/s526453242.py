x=0
W=input()
S=""
while True:
    S=input()
    if S=="END_OF_TEXT":
        break
    S=S.lower().split()
    x+=S.count(W)
print(x)