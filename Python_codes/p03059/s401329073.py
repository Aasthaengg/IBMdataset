A,B,T = map(int,input().split())

print(sum([B if(i%A==0) else 0 for i in range(A,T+1)]))
