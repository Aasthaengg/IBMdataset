N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print('Yes' if sum(B)-sum(A)>=sum(max(0,(b-a+1)//2) for a,b in zip(A,B)) else 'No')