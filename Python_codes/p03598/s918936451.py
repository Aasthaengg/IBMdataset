N,K=int(input()),int(input())
x=list(map(int,input().split()))
a = [i*2 for i in x]
b = [(K-i)*2 for i in x]
print(sum([i if i < j else j for i,j in zip(a,b)]))