from collections import deque
k = int(input())
def solve():
  count = 0
  stack_strings = deque([str(i) for i in range(9, -1, -1)])
  for _ in range(10):
    for _ in range(len(stack_strings)):
      lunstring = stack_strings.pop()
      if lunstring[0] != "0":
        count += 1
        if count == k:
          return(int(lunstring))
      right_char = lunstring[-1]
      if right_char == "0":
        [stack_strings.appendleft(lunstring+x) for x in ["0", "1"]]
      elif right_char == "9":
        [stack_strings.appendleft(lunstring+x) for x in ["8", "9"]]
      else:
        [stack_strings.appendleft(lunstring+x) for x in [str(int(right_char)-1), right_char, str(int(right_char)+1)]]
print(solve())