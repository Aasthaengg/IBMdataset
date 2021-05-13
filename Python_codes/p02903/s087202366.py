import numpy as np
H,W,A,B=map(int, input().split())
S=np.array([["0"]*W for _  in range(H)])

S[:B, :A]="1"
S[B:, A:]="1"

for s in S:
    print("".join(s.tolist()))