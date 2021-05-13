A, B, C = map(int, input().split())

print(C+B if C<=A+B+1 else A+1+B*2)