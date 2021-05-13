n,m = map(int,input().split())
if n==1:
    wide = range(0,10)
else:
    wide = range(10**(n-1), 10**n)
st = set(wide)

for _ in range(m):
    s,c = map(int, input().split())
    lst = list(wide)
    st1 = set()
    if s==1 and c==0 and n != 1:
        st &= set()
    for i in wide:
        x = i // 10**(n-s)
        if x % 10 == c:
            st1.add(i)
    st &= st1

lst = list(st)
lst.sort()
lst.append(-1)
print(lst[0])