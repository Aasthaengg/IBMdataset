H_1, M_1, H_2, M_2, K = map(int, input().split())
time =(H_2 * 60 + M_2)-(H_1 * 60 + M_1)

if time <= K:
    print(0)
    exit(0)
else :
    print(time-K)