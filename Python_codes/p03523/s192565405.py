s = input()
possible = []
for i in range(2**4):
    st = "" 
    if i & 1 << 0:
        st += "A"
    st += "KIH"
    if i & 1 << 1:
        st += "A"
    st += "B"
    if i & 1 << 2:
        st += "A"
    st += "R"
    if i & 1 << 3:
        st += "A"
    possible.append(st)
if s in possible:
    print("YES")
else:
    print("NO")