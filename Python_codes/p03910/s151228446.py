N = int(input())
st = set()
s = 0
n = 1
while s < N:
    st.add(n)
    s += n
    n += 1
if s > N:
    st.remove(s-N)
print(*st, sep='\n')