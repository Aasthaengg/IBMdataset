N = int(input())
a = list(map(int,input().split()))
a.sort()
Answer = a[0] - 1
for i in range(1,N):
        Answer += a[i]-1
print(Answer)