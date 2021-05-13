
n,m,K=map(int,input().split());print("YNeos"[all(k*m-K+l*n-k*l*2for k in range(n+1)for l in range(m+1))::2])
