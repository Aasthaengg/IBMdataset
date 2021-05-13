A = int(input())
B = int(input())
C = int(input())
Y = int(input())

ra = min(A,int(Y//500+1))
rb = min(B,int(Y//100+1))
rc = min(C,int(Y//50+1))
#print(ra,rb,rc)

cnt = 0
for a in range(0,ra+1):
  for b in range(0,rb+1):
    for c in range(0,rc+1):
      if 500*a + 100*b + 50*c == Y:
        cnt += 1
        
print(cnt)