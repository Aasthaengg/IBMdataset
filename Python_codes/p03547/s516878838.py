x, y = input().split()
st = ['A','B','C','D','E','F']
xin = st.index(x)
yin = st.index(y)
if xin > yin:
    print('>')
elif xin < yin:
    print('<')
else:
    print('=')