n=int(input())
arr=list(map(int,input().split()))
diff=0
for i in range(n):
  if arr[i] != (i+1):
    diff+=1

print("YES" if diff==2 or diff==0 else "NO")
