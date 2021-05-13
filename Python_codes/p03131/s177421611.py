K,A,B = map(int,input().split())
bis = K+1
tempbis = 1
if A<B and A<K:
    tempbis=A
    K -= A-1
    tempbis += K%2
    tempbis += (B-A)*(K//2)

print(max(bis,tempbis))