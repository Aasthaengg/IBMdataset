calcs = ["+", "-", "*", "/"]

#a="1 2 + 3 4 - *"
#a="1 2 +"
#lst = a.split()
lst = raw_input().split()

st=[]

def calc(e):

    tot=0
    tmp=0
    first=True

    b = st.pop()
    a = st.pop()

    if e   == "+":
        tot = a + b
    elif e == "-":
         tot = a- b
    elif e == "*":
         tot = a * b
    elif e == "/":
         tot = a / b

    st.append(tot)

for x in lst:
    if x in calcs:
       calc(x)
    else:
       st.append(int(x))

print st.pop()