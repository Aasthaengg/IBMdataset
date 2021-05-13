A, B = map(int, input().split())
ans = 0
for i in range(A, B+1):
   num_rev = list(reversed(list(map(int, str(i)))))
   if int(''.join(map(str, num_rev))) == i:
       ans += 1

print(ans)