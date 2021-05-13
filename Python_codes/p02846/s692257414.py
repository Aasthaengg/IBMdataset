t1,t2 = list(map(int, input().split()))
a1,a2 = list(map(int, input().split()))
b1,b2 = list(map(int, input().split()))

ptr1 = (b1 - a1) * t1
ptr2 = ptr1 + (b2 - a2) * t2
ptr3 = ptr2 + (b1 - a1) * t1
ptr4 = ptr3 + (b2 - a2) * t2

if ptr2 == 0:
  ans = 'infinity'
elif ptr1 * ptr2 > 0:
  ans = 0
else:
  ans = 1 + 2 * (abs(ptr1) // abs(ptr2))
  if abs(ptr1) % abs(ptr2) == 0:
    ans -= 1

print(ans)