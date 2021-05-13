input()
g = input()
a = list(map(str, g.split()))
b = list(map(int, g.split()))
if sorted(b) == b:
    print("YES")
else:
    m = 0
    for i in range(len(b)):
        if b[i] == sorted(b)[i]:
            m+=1
    if m==len(b)-2:
        print("YES")
    else:
        print("NO")