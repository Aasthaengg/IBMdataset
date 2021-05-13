n = int(input())
st = []
for _ in range(n):
    st.append([str(i) for i in input().split()])
x = str(input())
y = 0
flag = False
ans = 0
for i in range(n):
    st[i][1] = int(st[i][1])
    if flag:
        ans += st[i][1]
    if st[i][0] == x:
        flag = True
print(ans)
