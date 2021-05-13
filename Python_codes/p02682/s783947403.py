A , B , C , K = map(int,input().split())

s = 0

mn = min(A, K)
s += mn 
K -= mn

mn = min(B, K)
K -= mn

mn = min(C, K)
s -=mn
K -= mn

print(s)