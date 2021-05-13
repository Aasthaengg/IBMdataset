N,K = map(int, input().split())
A = list(map(int, input().split()))


#２整数の最大公約数を求める

def gcd2(x,y): 
	while y != 0:
		x , y = y , x % y 
	return x



#N 整数の最大公約数を求める
#A = [A[0],...,A[N]] とする

def gcd(A):
    ans = A[0]
    for i in range(1,N): #range(1,N)= 1,2,...,N-1
        ans = gcd2(ans, A[i])
    return ans



g = gcd(A)
M = max(A)

if (K<= M) and (K%g == 0):
    print("POSSIBLE")
else: print("IMPOSSIBLE")