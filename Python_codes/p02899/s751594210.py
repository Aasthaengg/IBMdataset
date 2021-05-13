n = int(input())
a = list(map(int,input().split()))
b = [0]*n
for i,j in enumerate(a):
    b[j-1] = str(i+1)
print(" ".join(b))