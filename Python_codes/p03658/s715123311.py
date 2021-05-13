n,m=map(int, input().split(" "))
s= sorted(list(map(int, input().split(" "))))
print(sum(s[n-m:]))