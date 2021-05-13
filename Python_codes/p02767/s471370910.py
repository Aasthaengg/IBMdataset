n = input()
x = list(map(int,input().split()))
print(min(sum((i-j)**2 for j in x) for i in range(min(x),max(x)+1)))