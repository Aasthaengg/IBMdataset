import statistics as st

n = int(input())
d = list(map(int, input().split()))

c1 = st.median_low(d)
c2 = st.median_high(d)

print(abs(c1-c2))
