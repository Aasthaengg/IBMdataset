c = 0
result = 0
while True:
    st = raw_input()
    if c == 0:
        s_str = st
    elif 'END_OF_TEXT' == st:
        break
    elif c > 0:
        if s_str.lower() in st.lower():
            result = result + st.lower().split(' ').count(s_str.lower())
        else:
            pass
    c = c+1
print result