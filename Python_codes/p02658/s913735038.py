N = int(input())

lst = input().split()

ans = 1

if '0' in lst:
   ans = 0
else:
   for i in range(N):
      ans = ans * int(lst[i])
      if 10**18 < ans:
         ans = -1
         break

print(ans)