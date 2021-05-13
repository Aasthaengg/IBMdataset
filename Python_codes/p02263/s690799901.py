s = raw_input().split(' ')
st = []
for i in s:
    if i.isdigit():
        st.append(int(i))
    elif i == '+':
        tmp1 = st.pop()
        tmp2 = st.pop()
        st.append(int(tmp1 + tmp2))
    elif i == '-':
        tmp1 = st.pop()
        tmp2 = st.pop()
        st.append(int(tmp2 - tmp1))
    elif i=='*':
        tmp1 = st.pop()
        tmp2 = st.pop()
        st.append(int(tmp1 * tmp2))
print st[0]