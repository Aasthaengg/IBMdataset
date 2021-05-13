a,b,c = map(int,input().split())
ans = 0
for i in range(10 ** 5):
         if (a % 2 == 1) or (b % 2 == 1) or (c % 2 == 1):
                  print(ans)
                  exit()
         tmpa = a
         tmpb = b
         tmpc = c
         a = (tmpb // 2) + (tmpc // 2)
         b = (tmpc // 2) + (tmpa // 2)
         c = (tmpa // 2) + (tmpb // 2)
         ans += 1
print(-1)
