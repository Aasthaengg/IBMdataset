N = int(input())
A = list(map(int,input().split()))

count = 0
for i, a in enumerate(A):
    #i+1はaが好き
    if A[a-1] == i+1:
        count += 1
print(count//2)