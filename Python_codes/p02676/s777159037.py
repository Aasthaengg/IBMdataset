K = int(input())
S = input()
Sl = list(S)
if len(S) > K:
    for i in range(K):
        print(Sl[i],end="")
        
    print("...")
    
else:
    print(S)