S = input().split()
def SvM(H, A):
 n = 1
 while A * n < H:
      n += 1
 return(n)

print(SvM(int(S[0]), int(S[1])))