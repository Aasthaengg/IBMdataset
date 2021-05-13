s = input()

st = set()
for c in s:
    if c in st:
        print("no")
        exit()
    st.add(c)

print("yes")
