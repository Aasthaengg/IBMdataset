N, A, B = list(map(int, input().split()))
X= list(map(int, input().split()))

I = []
for i in range(N-1):
    I.append(X[i+1]-X[i])

M = X[N-1]-X[0]
I_srt = sorted(I)
I_srt.reverse()

I_sum = [0]
for i in range(N-1):
    I_sum.append(I_srt[i]+I_sum[i])


ans = min([(M-I_sum[i])*A + B*i for i in range(N)])

print(ans)

