H_1,M_1,H_2,M_2,K = map(int,input().split())
time_1 = H_1*60+M_1
time_2 = H_2*60+M_2
print(time_2-time_1-K)