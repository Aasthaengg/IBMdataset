x1, y1, x2, y2 = map(int, input().split())

#x_diff = 2 3 6 6
#diff = abs(x1-x2) if x1!=x2 else abs(y1-y2)

def up(x_pre, y_pre, x_diff, y_diff):
  return x_pre-x_diff, y_pre+y_diff
def left(x_pre, y_pre, x_diff, y_diff):
  return x_pre-x_diff, y_pre-y_diff
def down(x_pre, y_pre, x_diff, y_diff):
  return x_pre+x_diff, y_pre-y_diff
def right(x_pre, y_pre, x_diff, y_diff):
  return x_pre+x_diff, y_pre+y_diff

x_diff_ = x2 - x1
y_diff_ = y2 - y1
#print(x_diff_, y_diff_)
rotate = []
if y_diff_ >= 0:
  if x_diff_ >= 0:
    #print(1)
    rotate = [up, left]
  else:
    #print(2)
    rotate = [left, down]
else:
  if x_diff_ >= 0:
    #print(3)
    rotate = [right, up]
  else:
    #print(4)
    rotate = [down, right]
  
x3, y3 = rotate[0](x2, y2, abs(y2-y1), abs(x2-x1))
#print(abs(y2-y1), abs(x2-x1))
x4, y4 = rotate[1](x3, y3, abs(y3-y2), abs(x3-x2))
#print(abs(y3-y2), abs(x3-x2))
print(x3, y3, x4, y4)
  
