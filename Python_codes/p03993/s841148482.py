n = int(input())
a = list(map(int, input().split()))

st = set()
cnt = 0
for i, e in enumerate(a, 1):
    pair = min(i, e), max(i, e)
    if pair in st:
        cnt += 1
    else:
        st.add(pair)

print(cnt)
