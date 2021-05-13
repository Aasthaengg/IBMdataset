def add(x, y):
    return x+y

def diff(x, y):
    return x-y
    
def mul(x, y):
    return x*y
    
def div(x, y):
    return int(x/y)

op = {"+" : add , "-" : diff, "*" : mul, "/" : div}

st = input()
s = st.split()
while(not s[1] == '?'):
    print(op[s[1]](int(s[0]), int(s[2])))
    st = input()
    s = st.split() 