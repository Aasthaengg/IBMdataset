n,time = map(int,input().split())
t = list(map(int,input().split()))
stoptime = 0
nagaretime = 0
for i in range(n):
         if nagaretime < t[i]:
                  stoptime += t[i] - nagaretime
         nagaretime = t[i] + time
print(nagaretime - stoptime)

