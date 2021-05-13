from operator import itemgetter
n = int(input())
st = []
for i in range(n):
    x, l = map(int, input().split())
    st.append([x-l, x+l])
st.sort(key = itemgetter(1))

i = 1
last = 0
count = 1
while i < n:
    if st[i][0] >= st[last][1]:
        last = i
        count += 1
    i += 1
print(count)      