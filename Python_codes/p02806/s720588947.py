n = int(input())
st = []
for i in range(n):
    st.append(list(input().split()))
x = input()
t = 0
for i in range(n):
    if st[i][0] == x:
        temp = i
        break
for i in range(temp + 1, n):
    t += int(st[i][1])
print(t)