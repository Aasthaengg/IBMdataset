N,K=map(int,input().split());S=input();u=[S[0]]
for c in S:c==u[-1]or u.append(c)
print(len(S)-max(len(u)-2*K,1))