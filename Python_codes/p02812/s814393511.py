N=int(input())
S=input()
print(len([i for i in range(N-2) if S[i:i+3]=='ABC']))