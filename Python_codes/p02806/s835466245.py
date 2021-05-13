N = int(input())
st = []
for i in range(N):
    s,t = input().split()
    st.append((s,int(t)))
X = input()

tmp = -1
for i in range(N):
    if st[i][0] == X:
        tmp = i
        break

ans = 0
for i in range(tmp+1,N):
    ans += st[i][1]
print(ans)