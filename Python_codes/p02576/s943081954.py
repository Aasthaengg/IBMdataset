str_in = input()
num = [int(n) for n in str_in.split()]
num = num =list(map(int, str_in.strip().split()))
# X,T,N
#(N/X)*T
N = num[0]
X = num[1]
T = num[2]
if N%X == 0:
    print((N//X)*T)
else:
    print((N//X+1)*T)