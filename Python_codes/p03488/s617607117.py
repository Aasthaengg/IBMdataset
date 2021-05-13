import sys

def main():
  s = input()
  n = len(s)
  x, y = map(int, input().split())
  
  move = [0]
  for i in range(n):
    if s[i] == "F":
      move[-1] += 1
    else:
      move.append(0)
  
  move_x = move[2::2]
  move_y = move[1::2]
  move_a = move[0]
  
  for start, lis in zip([x-move_a, y], [move_x, move_y]):
    move_range = sum(lis)
    if abs(start) > move_range:
      print("No")
      sys.exit()
    
    dp = 2**move_range
    for value in lis:
      dp = (dp >> value)|(dp << value)
    if not (dp>>(move_range+start))&1:
      print("No")
      sys.exit()
  
  print("Yes")
  
  
if __name__ == "__main__":
  main()