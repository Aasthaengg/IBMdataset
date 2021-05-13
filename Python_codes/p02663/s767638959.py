H1, M1, H2, M2, K = map(int,input().split())

if H2 < H1:
    H2 = H2 + 24
if H1 == H2 and H2 < H1:
    H2 = H2 + 24


time2m = H2 * 60 + M2
time1m = H1 * 60 + M1

study_time = time2m - K - time1m

if study_time <= 0:
    print(0)
else:
    print(study_time)

