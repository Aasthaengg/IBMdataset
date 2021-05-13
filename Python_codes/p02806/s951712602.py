st = []
tt = []
for n in range(int(input())):
    s, t = input().split()
    t = int(t)

    st.append(s)
    tt.append(t)

x = input()

ans = 0
flag = 'no'
for i in range(n+1):
    if (flag == 'yes'):
        ans += tt[i]
        
    if st[i] == x:
        flag = 'yes'

print(ans)
