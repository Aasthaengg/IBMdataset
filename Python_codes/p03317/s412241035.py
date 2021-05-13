N, K = map(int,input().split())
AN = list(map(int,input().split()))
AN.sort()
N = N - AN.count(AN[0])

print( -(-N//(K-1)) )
