H1, M1, H2, M2, K = list(map(int, input().split()))
time = (H2-H1)*60+M2-M1
print(time-K)