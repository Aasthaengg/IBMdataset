N = int(input())
h = list(map(int,input().split()))
print(sum(max(0,h[x]-h[x+1]) for x in range(N-1)) + h[-1]) 

