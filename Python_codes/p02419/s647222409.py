W=raw_input().lower()
T=[]
while True:
    t=raw_input()
    if t=="END_OF_TEXT":
        break
    T+=t.lower().split()
print T.count(W)