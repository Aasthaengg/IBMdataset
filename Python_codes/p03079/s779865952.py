A,B,C = map(int, input().split())
print('Yes') if A+B>C and C+B>A and A+C>B and A==B and B==C else print('No')