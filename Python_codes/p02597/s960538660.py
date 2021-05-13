N = int(input())
C = input()

R_cnt = C.count('R')
print(C[:R_cnt].count('W'))