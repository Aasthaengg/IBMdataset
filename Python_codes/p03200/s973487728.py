S=input()
X=K=0
for i in range(1,len(S)+1):
    if S[i-1]=="W":
        X+=i
        K+=1
print(X-(K*(K+1))//2)
