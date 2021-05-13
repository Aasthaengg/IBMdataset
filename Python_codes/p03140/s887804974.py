N = int(input())
A = input()
B = input()
C = input()

count = 0

for i, j, k in zip(A,B,C):
    #print(set([i,j,k]))
    count = count + len(set([i,j,k])) - 1

print(count)