input();S=sorted(int(x)-i-1 for i,x in enumerate(input().split()))
print(sum(abs(S[len(S)//2]-s)for s in S))
