
N, K = map(int, input().split())
S = input()
S = S + "8"

a = []
f = S[0]
l = 0
for i in range(1, N+1):
    if f != S[i]:
        a.append(i-l)
        l = i
        f = S[i]
        

if S[0] == '0':
    a = [0] + a

SUM = sum(a[0:0+2*K+1])

MAX = max(0, SUM)
for i in range(2, len(a)):
    if i % 2 == 0:
        try:
            SUM = SUM - (a[i-2]+a[i-1]) + (a[i+2*K-1]+a[i+2*K])
        except:
            try:
                SUM = SUM - (a[i-2]+a[i-1]) + (a[i+2*K-1])
            except:
                break
        
        MAX = max(MAX, SUM)


print(MAX)