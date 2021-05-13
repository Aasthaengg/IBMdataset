#n = int(input())
#n,k = map(int,input().split())
#x = list(map(int,input().split()))
 
 
n,k = map(int,input().split())
print(max(n+k,n-k,n*k))