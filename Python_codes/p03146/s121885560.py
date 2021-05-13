s = int(input())


def f(n):
  if n%2==0:
    return n//2
  else:
    return 3*n+1

A = [s]
while True:
  a = f(A[-1])
  if a in A:
    ans = len(A) + 1
    break
  else:
    A.append(a)

# /print(A)
print(ans)

