n,a,b = map(int, input().split())
print(min(a-1, n-b)+1+(b-a-1)//2 if (b-a)%2!=0 else (b-a)//2)