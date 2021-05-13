#M-SOLUTIONS プロコンオープン b
s=input()
win=s.count('o')+max(0,15-len(s))
if win>=8:
    print("YES")
else:
    print("NO")