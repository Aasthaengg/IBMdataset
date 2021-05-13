S = list(input())
before = 0
last_upper = -1
count = 0
answer = 0
for i, s in enumerate(S):
  # print(answer, i, before, last_upper)
  if s == '<':
    if before < 0 and last_upper < i-1:
      answer += abs(before)*(i-last_upper)
      before = 0
    elif before > 0 and last_upper < i-1:
      answer -= before*(i-last_upper-1)
      before = 0
    before += 1
    answer += before
    last_upper = i
  else:
    before -= 1
    answer += before
# print(answer, before, last_upper)
if before < 0:
  answer += abs(before)*(len(S)-last_upper)
elif before > 0:
  answer -= before*(len(S)-last_upper-1)
print(answer)
