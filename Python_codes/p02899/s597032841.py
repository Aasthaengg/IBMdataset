N = int(input())
A = list(map(int, input().split()))
B = [0]*N

for i in range(len(A)):
    B[A[i]-1] = i+1

s = ""
for i in B:
    s = s + str(i) + " "

print(s.strip())
