n = int(input())
s = list(input())
f = lambda x:1 if x=='R' else -1
y = list(map(f, s))
if sum(y)>0:
    print("Yes")
else:
    print("No")
