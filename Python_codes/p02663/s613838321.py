def find(H1,M1,H2,M2,K):
    left = H1*60+M1
    right = H2*60+M2
    remain = right-left-K
    return max(remain,0)
H1,M1,H2,M2,K = list(map(int,input().strip().split()))
print(find(H1,M1,H2,M2,K))