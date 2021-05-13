N = int(input())
A = list(map(int, input().split()))
A = map( lambda x:x//400, A)
A = list(map( lambda x:x if x<8 else 8, A))
cnt8 = A.count(8)
A = list(set(A))
if 8 in A:
    A.remove(8)
sum = len(A)
if sum == 0:
    print(1, end=' ')
else:
    print(sum, end=' ')
sum += cnt8
print(sum)