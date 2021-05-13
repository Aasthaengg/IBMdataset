S = input()
def judge(S):
  memo = []
  for i in range(len(S)):
    if S[i] in memo:
      return False
    memo.append(S[i])
  return True

print("yes" if judge(S) else "no")