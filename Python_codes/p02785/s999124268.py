N,K = list(map(int,input().split()))
H = list(map(int,input().split()))

H.sort(reverse=True)

H=H[K:]

H_cumsum=[0]
H_sum_=0
for n in range(len(H)):
    H_sum_=H_sum_+H[n]
    H_cumsum.append(H_sum_)
print(H_sum_)