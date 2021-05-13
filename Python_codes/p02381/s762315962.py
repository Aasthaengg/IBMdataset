import statistics as st
while True:
    n = int(input())
    if n == 0:
        break
    x = tuple(map(float, input().strip().split()))
    y = st.mean(x)**2
    z = st.mean(map(pow, x, (2 for i in range(n))))
    print((z-y)**0.5)