N = int(input())
A = list(map(int,input().split()))
odd = 1
for i in A :
    if i%2==0:
        odd *= 2
    else :
        odd *= 1
print(3**N-odd)