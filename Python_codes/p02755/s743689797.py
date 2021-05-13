a,b = map(int, input().split())
ok = True
for i in range(1001):
  if int(i*0.08)==a and int(i*0.1)==b:
    print(i)
    ok = False
    break
if ok: print(-1)