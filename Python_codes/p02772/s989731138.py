N = input()
A = map(int, input().split())
ok = True
for a in A:
  if a % 2 == 0 and a % 3 and a % 5:
    ok = False
    break
print('APPROVED' if ok else 'DENIED')