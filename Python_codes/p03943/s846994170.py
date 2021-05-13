S = list(map(int,input().split()))
sorted_S = sorted(S)

if sorted_S[0] + sorted_S[1] == sorted_S[2]:
    print('Yes')
else:
    print('No')
    

