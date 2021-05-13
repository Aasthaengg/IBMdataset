N, M = map(int, input().split())
L, R = map(int, input().split())


for i in range(M-1):
      L1, R1 = map(int, input().split())
      if R1 < L or R < L1:
        print(0)
        exit()
      else:
        if L <= L1 <= R:
          L = L1
          
        elif L <= R1 <= R:
          R = R1
        
          
print(R-L+1)