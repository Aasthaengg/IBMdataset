s = input()
t = input()

s = sorted(s)
t = sorted(t)[::-1]

if s == t:
    print("No")
    exit()

st = []
st.append(s)
st.append(t)
st = sorted(st)

if st[0] == s:
    print("Yes")
else:
    print("No")
