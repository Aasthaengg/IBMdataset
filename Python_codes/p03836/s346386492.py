#!/usr/bin/env python3

# input = stdin.readline

def solve(sx,sy,tx,ty):
  res = []
  dx = tx - sx
  dy = ty - sy
  
  assert dx > 0 and dy > 0
  # 1回目
  res.extend(['R']*dx)
  res.extend(['U']*dy)
  res.extend(['L']*dx)
  res.extend(['D']*dy)

  # 2回目
  res.append('D')
  res.extend(['R']*(dx+1))
  res.extend(['U']*(dy+1))
  res.append('L')

  res.append('U')
  res.extend(['L']*(dx+1))
  res.extend(['D']*(dy+1))
  res.append('R')
  return ''.join(res)


def main():
  sx,sy,tx,ty = map(int,input().split())
  print('{}'.format(solve(sx,sy,tx,ty)))

if __name__ == '__main__':
  main()
