A,B=list(map(int,input().split()))
l_a=list(input())
l_b=list(input())
import fractions
gcd=fractions.gcd(A,B)
total=A*B//gcd
A_n=total//A
B_n=total//B
S=A_n*B_n//fractions.gcd(A_n,B_n)
for i in range(total//S):
   if l_a[i*B_n] != l_b[i*A_n]:
      print(-1)
      exit()
print(total)