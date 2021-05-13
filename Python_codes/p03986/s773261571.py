X = list(input())

st = []
for x in X:
    if x == 'S':
        st.append(x)
    else:
        if len(st) > 0 and st[-1] == 'S':
            st.pop()
        else:
            st.append(x)
print(len(st))
