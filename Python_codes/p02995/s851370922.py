import fractions
A, B, C, D = map(int, input().split())
n_C = B // C - (A-1) //C
n_D = B // D - (A-1) //D
n = (C * D) // fractions.gcd(C, D)
n_C_D = B // n - (A-1)// n
print(B-A-n_C-n_D+n_C_D+1)