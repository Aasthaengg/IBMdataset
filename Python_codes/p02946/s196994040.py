K,X = map(int,input().split())
candidatetop = min(X+K-1,1000000)
candidatedown = max(X-K+1,-1000000)
nums = [i for i in range(candidatedown,candidatetop+1)]
print(' '.join(map(str,nums)))