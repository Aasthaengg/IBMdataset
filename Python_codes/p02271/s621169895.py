n = int(raw_input())
A = map(int, raw_input().split())
q = int(raw_input())
m = map(int, raw_input().split())
nums = []

def func(i, p):
  if i != n:
    func(i+1, p)
    p += A[i]
    func(i+1, p)
  elif i == n:
    nums.append(p)

func(0, 0)

for i in range(q):
  if m[i] in nums:
    print("yes")
  else:
    print("no")