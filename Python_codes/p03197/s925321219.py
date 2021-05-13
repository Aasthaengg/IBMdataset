N = int(input())
ans = True
for i in range(N):
    ai = int(input())
    if ai % 2 != 0:
        ans = False
        break
        
if ans:
    print("second")
else:
    print("first")