A = int(input())
B = int(input())
C = int(input())
D = int(input())

#A通常電　Bのりほ電　C通常バス Dのりぼバス

A_C = (A+C)
A_D = (A+D)
B_C = (B+C)
B_D = (B+D)

print(min(A_C,A_D,B_C,B_D))