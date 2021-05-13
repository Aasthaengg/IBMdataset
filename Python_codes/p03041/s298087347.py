a,b=map(int,input().split())
n=input()
n=n[:b-1]+n[b-1].lower()+n[b:]
print(n)