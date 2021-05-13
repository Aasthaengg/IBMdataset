n = int(input())
a = list(map(int, input().split()))
a = [e for e in a if e % 2 == 0 ]
cnt = 0
for i in a:
    if not (i % 3 ==0) and not (i % 5 ==0):
        cnt = 1
        break
if cnt:
    print("DENIED")
else:
    print("APPROVED")