[N, A, B] = [int(i) for i in input().split()]
print(int(N/(A+B))*A + min(A, N - (A+B)*int(N/(A+B)) ))