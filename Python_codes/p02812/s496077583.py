N=int(input())
S=input()
print(sum(S[i]=='A' and S[i+1]=='B' and S[i+2]=='C' for i in range(N-2)))