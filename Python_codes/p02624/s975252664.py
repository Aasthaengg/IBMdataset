n=int(input())
print(sum([((n//i)*(i+(n//i*i))//2) for i in range(1,n+1)]))