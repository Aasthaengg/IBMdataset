N=int(input())
k=len(set(list(map(int,input().split()))))
print(k if k%2 else k-1)