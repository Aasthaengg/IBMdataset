n,k = map(int, input().split()) 
L = list(map(int,input().split())) 

L.sort() 
L_len = len(L) 
print(sum(L[-k:]))