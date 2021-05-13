N, Q = list(map(int,input().split()))
S = input()
A = []
B = []
for i in range(Q):
    in1, in2 = list(map(int,input().split()))
    A.append(in1)
    B.append(in2)
ac = [0]
for i in range(1, N):
    if S[i] == "C" and S[i - 1] == "A":
        ac.append(ac[-1] + 1)
    else:
        ac.append(ac[-1])
        
for i in range(Q):
    ans = ac[B[i] - 1] - ac[A[i] - 1]
    print(ans)